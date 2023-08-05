from bs4 import BeautifulSoup
import pandas as pd
import requests
from dateutil import parser
import datetime as dt 
import time
import random
from db.db import DataDB
#Scraping TradingEconomics Calendar Info from tradingeconomics.com/calendar

#Extract date from table's head
pd.set_option("display.max_rows", None)

def get_date(c):
    tr = c.select_one("tr")
    ths = tr.select("th")
    for th in ths:
        if th.has_attr("colspan"):
            date_text = th.get_text().strip()
            return parser.parse(date_text)
    return None

def get_data_point(key, element):
    for e in['span', 'a']:
        d = element.select_one(f"{e}#{key}")
        if d is not None:
            return d.get_text()
    return ''

def get_data_for_key(tr, key):
    if tr.has_attr(key):
        return tr.attrs[key]
    return ''

def get_data_dict(item_date, table_rows):
    data = []

    for tr in table_rows:
        data.append(dict(
            date = item_date,
            country = get_data_for_key(tr, 'data-country'),
            category = get_data_for_key(tr, 'data-category'),
            event = get_data_for_key(tr, 'data-event'),
            symbol = get_data_for_key(tr, 'data-symbol'),
            actual = get_data_point('actual', tr),
            previous = get_data_point('previous', tr),
            forecast = get_data_point('forecast', tr)
        ))

    return data

def get_fx_calendar(from_date):

    session = requests.Session()
    
    from_date_str = dt.datetime.strftime(from_date, "%Y-%m-%d 00:00:00")
    to_date = from_date + dt.timedelta(days=6)
    to_date_str = dt.datetime.strftime(to_date, "%Y-%m-%d 00:00:00")

    #Headers so website thinks we're human
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Cookie" : f"calendar-importance=3; cal-custom-range={from_date_str}|{to_date_str}; TEServer=TEIIS; cal-timezone-offset=0"
    }
    response = session.get('https://tradingeconomics.com/calendar', headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.select_one("table#calendar")

    #Iterate through each one of child elements of the table 
    #Until we hit new table head they belong to head's date
    #Second table head has class property hidden-head, so we'll take advantage of that property

    last_header_date = None #Most recent header 
    trs = {}
    final_data = []

    for c in table.children:
        if c.name == 'thead':
            if 'class' in c.attrs and 'hidden-head' in c.attrs['class']:
                continue #Skip hidden head (2nd table head)
            last_header_date = get_date(c)
            trs[last_header_date] = []
        elif c.name == "tr":
            trs[last_header_date].append(c)
    
    #Key - Date, Value - List of Table Rows
    for item_date, table_rows in trs.items():
        final_data += get_data_dict(item_date, table_rows)

    return final_data

def fx_calendar():
    #final_data = []

    start = parser.parse("2023-01-01T00:00:00Z")
    end = parser.parse("2023-08-10T00:00:00Z")

    database = DataDB()

    while start < end:
        data = get_fx_calendar(start)
        print(start, len(data))
        database.add_many(DataDB.CALENDAR_COL, data)
        start = start + dt.timedelta(days=7)
        time.sleep(random.randint(1,4)) #Looks like human is going to sites not exactly 1 second every time
    
    #print(pd.DataFrame.from_dict(final_data))