#TO REVISE OR DELETE


from flask import Flask, Response, render_template, request, jsonify
import json
import requests
import time
import unidecode
import random

app = Flask(__name__)

#I edited the progam I used on the Alexa app to make fetchDict() so I'm not actually certain as to what some of the code does, but it works

def fetchDict():
	user_pass_dict = {"api_type": "json"}
	sess = requests.Session()
	sess.headers.update({'User-Agent': 'Fetching article headlines'})
	sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
	#Apparently reddit is picky about requests so the time.sleep just assures that we don't get kicked off or something
	time.sleep(.25)
	url = "https://www.reddit.com/r/worldnews/.json?limit=500"
	html = sess.get(url)
	data = json.loads(html.content.decode('utf-8'))
	newsDict = {}
	#The main loop that pairs the title and score ONLY IF the score is over 100.
	#For whatever reason I'm only able to grab a limited number of articles
	#so the list is pretty small, that is somthing we'll have to expand in the future. 
	for listing in data['data']['children']:
		headline = [unidecode.unidecode(listing['data']['title'])]
		score = [unidecode.unidecode(str(listing['data']['score']))]
		include = False
		if int(score[0]) >= 100:
			include = True
		if include:
			newsDict[headline[0]] = score[0]
  
	return newsDict
@app.route('/')

def homepage():
	return render_template("index.html")

#Just copied what I did for the shopping assignment, I am not sure if this is what we're going for or not. 
@app.route('/getNewsDict')
def news():
	newsDict = fetchDict()
	return jsonify(newsDict)

if __name__=='__main__':
	app.run(debug=True, port=5001)
