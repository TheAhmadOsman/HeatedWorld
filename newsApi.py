import json
import requests
import time
import random


class newsApi:
    def __init__(self, time):
        #time is represented in seconds
        self.time = time

    def fetchNews(self):
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=us&'
               'apiKey=secret')
        response = requests.get(url)
        print(response.json())


x = newsApi(1)
x.fetchNews()
