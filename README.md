# FXGuru

FXGuru is a live 24/7 algorithmic forex trading bot that uses the best-known forex indicators and candle patterns to place and close trades on the Oanda trading platform. In addition to being a bot, FXGuru also contains an advanced backtesting system that can be used to evaluate the strength of particular forex trading strategies by calculating these strategies' cumulative gains over a desired range of historical data from the Oanda API. Lastly, FXGuru contains a [web application](https://fxguru.netlify.app) that scrapes market sentiment and provides both graphical and technical analysis of recent price changes in over 40 different currency pairs!

## Contents

- [Description](#description)

    - [Bot](#bot)
    - [Backtesting System](#backtesting-system)
    - [Web Application](#web-application)

- [Technologies](#technologies)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Author](#author)

## Description

### Bot

FXGuru's live trading bot is powered by 3 main functions:
 
 - Candle Manager - Checks to see if a new candle has loaded from the Oanda API and if there has been a new candle, the candle manager loads and processes the candle

 - Technical Manager - Identifies if a trading signal has been indicated from the newly processed candles that the Candle Manager passed. The default trading signal used is the Bollinger Bands forex indicator, but this can be changed to any of the indicators/candle patterns which are discussed in the Advanced Backtesting System.

 - Trade Manager - If there is already an existing open trade or a minimum gain has not been met yet, then FXGuru will not place a new trade. Trade Manager will close an open trade once it has reached its fixed stop loss or take profit value, and then proceed to place a new trade.

FXGuru also utilizes multithreading to stream live prices of currency pairs to their respective logs. The bot can run multiple currency pair threads in parallel and processes these pairs' price information at once which greatly optimizes performance.

### Backtesting System

FXGuru's Advanced Backtesting System contains all of the following forex indicators and candle patterns. These indicators and patterns can be grouped and modified to test almost any forex trading strategy that is discussed.

#### Forex Indicators:
- Bollinger Bands
- Average True Range (ATR)
- Keltner Channels
- Relative Strength Index (RSI)
- Moving Average Convergence/Divergence (MACD)

#### Candle Patterns:
- Hanging Man
- Shooting Star
- Spinning Top
- Marubozu
- Engulfing
- Tweezer Top
- Tweezer Bottom
- Morning Star
- Evening Star

I used this backtesting system to test 2 popular "guaranteed" winning trading strategies from Youtube by testing their cumulative gains from 2016-2022 (using data from Oanda's API) and after accounting for spread both these strategies were far from what they preached. 

### Web application

[FXGuru's web application](https://fxguru.netlify.app) showcases the status of the live bot by displaying the details of your Oanda trading account. Additionally, there is a dashboard section which displays both a technical analysis and graphical analysis of 40 different currency pairs with 4 candlestick time frames over the past 50, 100, or 200 time frames. The website also contains  headlines which display scraped market sentiment from [Reuters](https://www.reuters.com/business/finance/). 

## Technologies

The technologies/frameworks that I used to build FXGuru were:

- Python 3.11.4 - Used throughout whole project except for Web App's frontend
- Pandas 2.0.3 - Used Pandas dataframes to represent and analyze historical price data
- Plotly 5.15.0 - Used to create candlestick charts and graph the forex indicators and candle patterns contained in the backtesting system
- Jupyter 1.0.0 - Platform where I could clearly visualize the Pandas dataframes, Plotly graphs, and Backtesting results
- Pymongo 4.4.1 - Used MongoDB to load and store both instrument (currency pair) data and scraped calendar data from the Oanda API and [Trading Economics](https://tradingeconomics.com/calendar) respectively
- Beautiful Soup 4.12.2 - Used to scrape data from [DailyFX](https://www.dailyfx.com/sentiment), [Investing.com](https://www.investing.com/technical/technical-analysis), [Reuters.com](https://www.reuters.com/business/finance/), and [TradingEconomics](https://tradingeconomics.com/calendar) 
- React 18.2.0 - Used to create Web App's frontend
- Plotly JS-dict 2.25.1 - Used to display the past 50, 100, or 200 time frames price data for currency pairs on Web App
- Flask 2.3.2 - Used for Web App's backend

## Screenshots

Below are screenshots of the [Web Application](https://fxguru.netlify.app/) and the Bot:

Home Page:

![Home](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru.netlify.app_.png?raw=true)

Headlines (Direct link to article):

![Headlines](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-home.png?raw=true)

Dashboard - Selection Options for Currency Pairs

![Options-Pairs](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-options-pairs.png?raw=true)

Dashboard - Selection Options for Candlestick Timeframes

![Options-Timeframes](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-options-timeframes.png?raw=true)

Dashboard Graph - Last 50 days

![Dashboard-50](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-dashboard-50.png?raw=true)

Dashboard Graph - Last 100 days

![Dashboard-100](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-dashbaord-100.png?raw=true)

Dashboard Graph - Last 200 days

![Dashboard-200day](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-dashboard-200day.png?raw=true)

Dashboard Graph - Last 1000 minutes (Past 200 5 min. time frames)

![Dashboard-200min5](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-dashboard-200min5.png)

Dashboard Graph - Analyze each individual candlestick

![Dashboard-graphanalysis](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-dashboard-graphanalysis.png?raw=true)

Bot (Will automatically create log file when run) - Main Log

![Bot-mainlog](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-bot-mainlog.png?raw=true)

Bot - Example GBP_JPY Log

![Bot-gbpjpylog](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-bot-gbpjpylog.png?raw=true)

Bot - Example EUR_GBP log

![Bot-eurgbplog](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-bot-eurgbplog.png?raw=true)

Bot - Trades going through on Oanda Trading Platform:

![bot-oanda1](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-bot-oanda1.png?raw=true)

![bot-oanda2](https://github.com/amoghmahadevan/fxguru/blob/main/fxguru-screenshots/fxguru-bot-oanda2.png?raw=true)


## Getting Started
To run FXGuru on your localhost follow the steps down below:

### Cloning the repository

```bash
git clone git@github.com:amoghmahadevan/fxguru.git
```

### Creating a virtual environment

After navigating to the root directory create and activate a python virtual environment

Creating a venv:

```bash
python3 -m venv venv
```
To activate the venv:

```bash
source venv/bin/activate
```

### Installing

To install all Python and JS requirements needed to run FXGuru:

```bash
pip install -r requirements.txt
cd fxguru-react
npm install
```

### Creating your constants and .env file

In the root directory, create a new folder named constants and create a file inside this folder named defs.py

Inside defs.py copy and paste the following template and make sure to enter your own Oanda API Key, Account Number, and MongoDB connection string

```py
API_KEY = "<Enter your Oanda Account API Key>"
ACCOUNT_ID = "<Enter your Oanda Account ID>"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SELL = -1
BUY = 1
NONE = 0

MONGO_CONNECTION_STRING ="<Mongo Connection String from your newly created cluster>"

INVESTING_COM_PAIRS = {
   "EUR_USD":{
      "pair":"EUR_USD",
      "pair_id":1
   },
   "GBP_USD":{
      "pair":"GBP_USD",
      "pair_id":2
   },
   "USD_JPY":{
      "pair":"USD_JPY",
      "pair_id":3
   },
   "USD_CHF":{
      "pair":"USD_CHF",
      "pair_id":4
   },
   "AUD_USD":{
      "pair":"AUD_USD",
      "pair_id":5
   },
   "EUR_GBP":{
      "pair":"EUR_GBP",
      "pair_id":6
   },
   "USD_CAD":{
      "pair":"USD_CAD",
      "pair_id":7
   },
   "NZD_USD":{
      "pair":"NZD_USD",
      "pair_id":8
   },
   "EUR_JPY":{
      "pair":"EUR_JPY",
      "pair_id":9
   },
   "EUR_CHF":{
      "pair":"EUR_CHF",
      "pair_id":10
   },
   "GBP_JPY":{
      "pair":"GBP_JPY",
      "pair_id":11
   },
   "GBP_CHF":{
      "pair":"GBP_CHF",
      "pair_id":12
   },
   "CHF_JPY":{
      "pair":"CHF_JPY",
      "pair_id":13
   },
   "CAD_CHF":{
      "pair":"CAD_CHF",
      "pair_id":14
   },
   "EUR_AUD":{
      "pair":"EUR_AUD",
      "pair_id":15
   },
   "EUR_CAD":{
      "pair":"EUR_CAD",
      "pair_id":16
   },
   "USD_ZAR":{
      "pair":"USD_ZAR",
      "pair_id":17
   },
   "USD_TRY":{
      "pair":"USD_TRY",
      "pair_id":18
   },
   "EUR_NOK":{
      "pair":"EUR_NOK",
      "pair_id":37
   },
   "BTC_NZD":{
      "pair":"BTC_NZD",
      "pair_id":38
   },
   "USD_MXN":{
      "pair":"USD_MXN",
      "pair_id":39
   },
   "USD_PLN":{
      "pair":"USD_PLN",
      "pair_id":40
   },
   "USD_SEK":{
      "pair":"USD_SEK",
      "pair_id":41
   },
   "USD_SGD":{
      "pair":"USD_SGD",
      "pair_id":42
   },
   "USD_DKK":{
      "pair":"USD_DKK",
      "pair_id":43
   },
   "EUR_DKK":{
      "pair":"EUR_DKK",
      "pair_id":44
   },
   "EUR_PLN":{
      "pair":"EUR_PLN",
      "pair_id":46
   },
   "AUD_CAD":{
      "pair":"AUD_CAD",
      "pair_id":47
   },
   "AUD_CHF":{
      "pair":"AUD_CHF",
      "pair_id":48
   },
   "AUD_JPY":{
      "pair":"AUD_JPY",
      "pair_id":49
   },
   "AUD_NZD":{
      "pair":"AUD_NZD",
      "pair_id":50
   },
   "CAD_JPY":{
      "pair":"CAD_JPY",
      "pair_id":51
   },
   "EUR_NZD":{
      "pair":"EUR_NZD",
      "pair_id":52
   },
   "GBP_AUD":{
      "pair":"GBP_AUD",
      "pair_id":53
   },
   "GBP_CAD":{
      "pair":"GBP_CAD",
      "pair_id":54
   },
   "GBP_NZD":{
      "pair":"GBP_NZD",
      "pair_id":55
   },
   "NZD_CAD":{
      "pair":"NZD_CAD",
      "pair_id":56
   },
   "NZD_CHF":{
      "pair":"NZD_CHF",
      "pair_id":57
   },
   "NZD_JPY":{
      "pair":"NZD_JPY",
      "pair_id":58
   },
   "USD_NOK":{
      "pair":"USD_NOK",
      "pair_id":59
   }
}

TFS = {
   "M5": 300,
   "M15": 900,
   "H1": 3600,
   "D": 86400
}

```

Navigate to the fxguru-react directory and create a .env file with the following api url:

```js
REACT_APP_API_URL = http://127.0.0.1:5000/api
```

### Running the application

#### Running the Bot:
```bash
python run_bot.py
```

#### Running the Web App:
Flask Backend:
```bash
python server.py
```
React Frontend (In fxguru-react directory):
```bash
npm run start
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Authors

[@amoghmahadevan](https://github.com/amoghmahadevan)
