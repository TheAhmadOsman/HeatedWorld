import json
import requests
import time
import unidecode
import random

class fetchData:
	def __init__(self, time):
		#time is represented in seconds
		self.time = time
	
	def fetch(self):
		user_pass_dict = {"api_type": "json"}
		sess = requests.Session()
		sess.headers.update({'User-Agent': 'Fetching article headlines'})
		sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
		#Apparently reddit is picky about requests so the time.sleep just assures that we don't get kicked off or something
		time.sleep(.25)
		url = "https://www.reddit.com/r/worldnews/.json?"
		html = sess.get(url)
		data = json.loads(html.content.decode('utf-8'))
		newsDict = {}
		#The main loop that pairs the title and score ONLY IF the score is over 100.
		#For whatever reason I'm only able to grab a limited number of articles
		#so the list is pretty small, that is somthing we'll have to expand in the future.
		targetTime = time.time() - self.time
		for listing in data['data']['children']:
			headline = [unidecode.unidecode(listing['data']['title'])]
			score = [unidecode.unidecode(str(listing['data']['score']))]
			utc = [unidecode.unidecode(str(listing['data']['created_utc']))]
			if int(score[0]) >= 100:
				if float(utc[0]) >= targetTime:
					newsDict[headline[0]] = score[0]
		return newsDict
#number represents 7 days
test = fetchData(604800)
titles = test.fetch()
print(len(titles))
