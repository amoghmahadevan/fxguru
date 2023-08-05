from bs4 import BeautifulSoup
import pandas as pd
import requests

#Scraping IG Client Sentiment Data from dailyfx.com/sentiment

def dailyfx_com():
    response = requests.get('https://www.dailyfx.com/sentiment')

    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.select(".dfx-technicalSentimentCard") 

    #Dictionary for scraped data
    pair_data = []

    for r in rows: 
        #Card containing pair name/sentiment
        card = r.select_one(".dfx-technicalSentimentCard__pairAndSignal")
        #Percent Change Value Row
        change_values = r.select(".dfx-technicalSentimentCard__changeValue")
        pair_data.append(dict(
            pair = card.select_one('a').get_text().replace("/", "_"),
            sentiment = card.select_one('span').get_text(),
            daily_change_longs = change_values[0].get_text(),
            daily_change_shorts = change_values[1].get_text(),
            weekly_change_longs = change_values[3].get_text(),
            weekly_change_shorts = change_values[4].get_text()
        ))
    #Creating dataframe from dictionary 
    return pd.DataFrame.from_dict(pair_data)

