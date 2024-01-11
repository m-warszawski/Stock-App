from django.db import models

class News():
    def __init__(self, title, url, time_published, authors, summary, source, 
                 topics, overall_sentiment_score, overall_sentiment_label):
        self.title = title
        self.url = url
        self.time_published = time_published
        self.authors = authors
        self.summary = summary
        self.source = source
        self.topics = topics
        self.overall_sentiment_score = overall_sentiment_score
        self.overall_sentiment_label = overall_sentiment_label


class SetOfNews():
    def __init__(self, number_of_items, sentiment_score_definition, 
                 relevance_score_definition, feed):
        self.number_of_items = number_of_items
        self.sentiment_score_definition = sentiment_score_definition
        self.relevance_score_definition = relevance_score_definition
        self.feed = feed


class Commodities():
    def __init__(self, name, interval, unit, datapoints):
        self.name = name
        self.interval = interval
        self.unit = unit
        self.datapoints = datapoints

class Forex():
    def __init__(self, from_currency_code, from_currency_name, to_currency_code, to_currency_name, exchange_rate):
        self.from_currency_code = from_currency_code
        self.from_currency_name = from_currency_name
        self.to_currency_code = to_currency_code
        self.to_currency_name = to_currency_name
        self.exchange_rate = exchange_rate