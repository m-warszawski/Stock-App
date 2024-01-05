from django.shortcuts import render
from dotenv import load_dotenv
from .models import SetOfNews, News, Commodities, Forex
import os
import requests

def index(request):

    forex_data = get_forex()
    commodities_data = get_commodities()
    news = get_news()

    return render(request, 'index.html', {'data': [commodities_data]})
    
def get_forex():

    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    forex_data_sets = []

    # api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey=',
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=PLN&apikey=',
    #             'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=PLN&apikey=',
    #            'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=AED&to_currency=PLN&apikey=']

    api_urls = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo']

    for url in api_urls:
        #r = requests.get(url+API_KEY)
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

    return(forex_data_sets)

def get_commodities():

    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    commodities_set = []

    # api_urls = ['https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=',
    #             'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=',
    #             'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=',
    #            'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=']

    api_urls = ['https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo',
                 'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo',
                 'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo',
                'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo']
    
    for url in api_urls:
        #r = requests.get(url+API_KEY)
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

        print(name)
        print(interval)
        print(unit)
        print(datapoints)
        print('...')

    return(commodities)

def get_news():

    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'#+API_KEY
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
    return(set1)

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
        overall_sentiment_label =""

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

    return(news)
