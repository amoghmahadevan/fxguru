import pandas as pd
import cloudscraper
import datetime as dt
import time 
from constants.defs import INVESTING_COM_PAIRS, TFS
#Scraping Technical Analysis section of investing.com
data_keys = ['pair_name',
             'studies_summary_color',
             'ti_buy', 
             'ti_sell', 
             'ma_buy', 
             'ma_sell', 
             'S1', 'S2', 'S3', 
             'pivot', 
             'R1', 'R2', 'R3', 
             'percent_bullish', 'percent_bearish']

#Creates key-value pairs of characteristic and its value
def get_data_object(text_list, pair_id, time_frame):
    data = {}
    data['pair_id'] = pair_id
    data['time_frame'] = time_frame
    data['updated'] = dt.datetime.utcnow()

    for item in text_list:
        temp_item = item.split("=")
        if len(temp_item) == 2 and temp_item[0] in data_keys:
            data[temp_item[0]] = temp_item[1]
    
    if 'pair_name' in data:
        data['pair_name'] = data['pair_name'].replace('/', "_")

    return data

def investing_com_fetch(pair_id, time_frame):
    #Newly updated to bypass CloudFare
    scraper = cloudscraper.create_scraper()

    #headers so that website thinks we're human
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    #Can easily modify for different currency pairs and time frames
    params = dict(
        action = 'get_studies',
        pair_ID = pair_id,
        time_frame = time_frame
    )
    #Network -> REQUEST URL
    response = scraper.get("https://www.investing.com/common/technical_studies/technical_studies_data.php", params=params, headers= headers)

    #No need of beautiful soup because already in string format
    text = response.content.decode("utf-8")

    index_start = text.index("pair_name=")
    index_end = text.index("*;*quote_link")
    #Substring for information we need
    data_str = text[index_start:index_end]

    #Dictionary for characteristic (key), and its value
    return get_data_object(data_str.split('*;*'), pair_id, time_frame)

def investing_com():
    data = []
    for pair_id in range(1, 12):
        for time_frame in [3600, 86400]:
            print(pair_id, time_frame)
            data.append(investing_com_fetch(pair_id, time_frame))
            time.sleep(0.5) #To prevent spamming server from requests
    
    return pd.DataFrame.from_dict(data)

def get_pair(pair_name, tf):
    if tf not in TFS:
        tf = TFS['H1']
    else:
        tf = TFS[tf]

    if pair_name in INVESTING_COM_PAIRS:
        pair_id = INVESTING_COM_PAIRS[pair_name]['pair_id']
        return investing_com_fetch(pair_id, tf)