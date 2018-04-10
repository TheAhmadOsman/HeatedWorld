import json
import requests
import time
import unidecode
import random
from operator import itemgetter


class Reddit:
    def __init__(self, time, key, subReddit):
        #time is represented in seconds
        self.time = time
        self.key = key
        self.subReddit = subReddit

    def fetch(self):
        user_pass_dict = {'usr': "secret", "passwd": "secret",
                          "api_type": "json"}
        sess = requests.Session()
        sess.headers.update({'User-Agent': 'Fetching article headlines'})
        sess.post('https://www.reddit.com/api/login', data=user_pass_dict)
        # Apparently reddit is picky about requests so the time.sleep just assures that we don't get kicked off or something
        time.sleep(.25)
        url = "https://www.reddit.com/r/%s/.json?limit=100" % (self.subReddit)
        html = sess.get(url)
        data = json.loads(html.content.decode('utf-8'))
        newsDict = {}
        # The main loop that pairs the title and score ONLY IF the score is over 100.
        # For whatever reason I'm only able to grab a limited number of articles
        # so the list is pretty small, that is somthing we'll have to expand in the future.
        targetTime = time.time() - self.time
        newsList = []

        for listing in data['data']['children']:
            headline = [unidecode.unidecode(listing['data']['title'])]
            score = [unidecode.unidecode(str(listing['data']['score']))]
            utc = [unidecode.unidecode(str(listing['data']['created_utc']))]
            url = [unidecode.unidecode(str(listing['data']['url']))]

            if int(score[0]) >= 100:
                newsList.append(
                    [headline[0], int(score[0]), float(utc[0]), url[0]])
        newsList.sort(key=itemgetter(1), reverse=True)
        count = 0
        for item in newsList:
            count += 1
            newsDict[count] = item
        return newsDict


# number represents 7 days
test = Reddit(604800, None, "worldnews/top")
titles = test.fetch()
print(len(titles))
