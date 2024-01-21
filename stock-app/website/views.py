from django.shortcuts import render
from dotenv import load_dotenv
from .models import SetOfNews, News, Commodities, Forex, Indicator, Stock
import os
import requests
from datetime import datetime


def index(request):
    stocks_data = get_stocks()
    indicators_data = get_indicators()
    forex_data = get_forex()
    commodities_data = get_commodities()
    news_data = get_news()
    crypto_data = get_crypto()

    return render(request, 'index.html', {'commodities': [commodities_data], 'forex': forex_data, 'news': [news_data],
                                          'crypto': crypto_data, 'indicators': [indicators_data], 'stocks': [stocks_data]})


def get_forex():
    load_dotenv()
    API_KEY = os.getenv('API_KEY2')

    forex_data_sets = []

    # api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=PLN&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=PLN&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=AED&to_currency=PLN&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=DOGE&to_currency=USD&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USDT&to_currency=USD&apikey='+API_KEY2]

    api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo',
                'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo']

    for url in api_urls:

        r = requests.get(url)
        data = r.json()

        from_currency_code = ""
        from_currency_name = ""
        to_currency_code = ""
        to_currency_name = ""
        exchange_rate = ""

        for key, value in data.items():

            if type(value) == str:
                break

            for k, v in value.items():
                if k == '1. From_Currency Code':
                    from_currency_code = v
                if k == '2. From_Currency Name':
                    from_currency_name = v
                if k == '3. To_Currency Code':
                    to_currency_code = v
                if k == '4. To_Currency Name':
                    to_currency_name = v
                if k == '5. Exchange Rate':
                    exchange_rate = v
                else:
                    pass

        forex = Forex(from_currency_code=from_currency_code, from_currency_name=from_currency_name,
                      to_currency_code=to_currency_code, to_currency_name=to_currency_name, exchange_rate=exchange_rate)

        forex_data_sets.append(forex)

    return (forex_data_sets)


def get_commodities():
    load_dotenv()
    API_KEY = os.getenv('API_KEY2')

    commodities_set = []

    # api_urls = ['https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey='+API_KEY2,
    #             'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey='+API_KEY,2
    #             'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey='+API_KEY2]

    api_urls = ['https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo',
                'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo',
                'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo',
                'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo']

    for url in api_urls:
        r = requests.get(url)
        data = r.json()

        name = ""
        interval = ""
        unit = ""
        datapoints = []

        for key, value in data.items():
            if key == 'name':
                name = value
            if key == 'interval':
                interval = value
            if key == 'unit':
                unit = value
            if key == 'data':
                datapoints = value

        commodities = Commodities(name=name, interval=interval, unit=unit, datapoints=datapoints)
        commodities_set.append(commodities)

    return (commodities_set)


def get_crypto():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    crypto_data_sets = []

    api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo']
    
    # api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+API_KEY,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey='+API_KEY,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=DOGE&to_currency=USD&apikey='+API_KEY,
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USDT&to_currency=USD&apikey='+API_KEY]


    for url in api_urls:
        r = requests.get(url)
        data = r.json()

        from_currency_code = ""
        from_currency_name = ""
        to_currency_code = ""
        to_currency_name = ""
        exchange_rate = ""

        for key, value in data.items():

            if type(value) == str:
                break

            for k, v in value.items():
                if k == '1. From_Currency Code':
                    from_currency_code = v
                if k == '2. From_Currency Name':
                    from_currency_name = v
                if k == '3. To_Currency Code':
                    to_currency_code = v
                if k == '4. To_Currency Name':
                    to_currency_name = v
                if k == '5. Exchange Rate':
                    exchange_rate = v
                else:
                    pass

        crypto = Forex(from_currency_code=from_currency_code, from_currency_name=from_currency_name,
                      to_currency_code=to_currency_code, to_currency_name=to_currency_name, exchange_rate=exchange_rate)

        crypto_data_sets.append(crypto)

        return(crypto_data_sets)


def get_indicators():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    indicators_set = []

    api_urls = ['https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=demo',
                'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey=demo',
                'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=demo',
                'https://www.alphavantage.co/query?function=INFLATION&apikey=demo',
                'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=demo']
    
    #api_urls = ['https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=INFLATION&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey='+API_KEY]

    for url in api_urls:
        r = requests.get(url)
        data = r.json()

        name = ""
        interval = ""
        unit = ""
        datapoints = []

        for key, value in data.items():
            if key == 'name':
                name = value
            if key == 'interval':
                interval = value
            if key == 'unit':
                unit = value
            if key == 'data':
                datapoints = value

        indicator = Indicator(name=name, interval=interval, unit=unit, datapoints=datapoints)
        indicators_set.append(indicator)

    return(indicators_set)


def get_stocks():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    stocks_set = []

    api_urls = ['https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo']

    #api_urls = ['https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NVDA&apikey='+API_KEY,
    #            'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey='+API_KEY]

    for url in api_urls:
        r = requests.get(url)
        data = r.json()

        symbol = ''
        opening = ''
        high = ''
        low = ''
        price = ''
        volume = ''
        latest_trading_day = ''
        previous_close = ''
        change = ''
        change_percent = ''

        for key, value in data.items():

            if type(value) == str:
                break

            for k, v in value.items():
                if k == '01. symbol':
                    symbol = v
                if k == '02. open':
                    opening = v
                if k == '03. high':
                    high = v
                if k == '04. low':
                    low = v
                if k == '05. price':
                    price = v
                if k == '06. volume':
                    volume = v
                if k == '07. latest trading day':
                    latest_trading_day = v
                if k == '08. previous close':
                    previous_close = v
                if k == '09. change':
                    change = v
                if k == '10. change percent':
                    change_percent = v
                else:
                    pass

        stock = Stock(symbol=symbol, opening=opening, high=high, low=low, price=price, volume=volume,
                      latest_trading_day=latest_trading_day, previous_close=previous_close, change=change,
                      change_percent=change_percent)
        stocks_set.append(stock)
        
    return(stocks_set)


def get_news():
    load_dotenv()
    API_KEY = os.getenv('API_KEY2')

    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'
    #url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=TSLA&apikey='+API_KEY2
    r = requests.get(url)
    data = r.json()

    number_of_items = 0
    sentiment_score_definition = ""
    relevance_score_definition = ""
    feed = []

    for key, value in data.items():
        if key == "items":
            number_of_items = value
        if key == "sentiment_score_definition":
            sentiment_score_definition = value
        if key == "relevance_score_definition":
            relevance_score_definition = value
        if key == "feed":
            feed = value

    process_news(feed)

    set1 = SetOfNews(number_of_items, sentiment_score_definition,
                     relevance_score_definition, feed)
    return (set1)


def process_news(feed):
    news = []

    for element in feed:

        title = ""
        url = ""
        time_published = ""
        authors = []
        summary = ""
        source = ""
        topics = ""
        overall_sentiment_score = ""
        overall_sentiment_label = ""

        for key, value in element.items():
            if key == "title":
                title = value
            if key == "url":
                url = value
            if key == "time_published":
                time_published = value
            if key == "authors":
                authors = value
            if key == "summary":
                summary = value
            if key == "source":
                source = value
            if key == "topics":
                topics = value
            if key == "overall_sentiment_score":
                overall_sentiment_score = value
            if key == "overall_sentiment_label":
                overall_sentiment_label = value
            else:
                pass

        n = News(title, url, time_published, authors, summary,
                 source, topics, overall_sentiment_score, overall_sentiment_label)
        news.append(n)

    return (news)

