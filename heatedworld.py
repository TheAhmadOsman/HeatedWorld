#############################################################################
#   Author: Ahmad M. Osman                                                  #
#   Date: 04/17/2018                                                        #
#                                                                           #
#   Project: HeatedWorld                                                    #
#   Purpose: World News' Heated Map.                                        #
#                                                                           #
#                           https://www.heated.world                        #
#                  https://github.com/Ahmad-Magdy-Osman/HeatedWorld         #
#                                                                           #
#   Filename: heatedworld.py                                                #
#   File overview: This file executes all necessary steps to prepare        #
#                       the news to be visualized on Heated.World           #
#                                                                           #
#############################################################################

import logging
import time
import json
import requests
import atexit
import os
import datetime
from collections import Counter
from flask import Flask, Response, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from reddit import Reddit

# Disables tensorflow warnings - doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)


def heatmap_json(day, week):
    logging.info("Ongoing...")

    # Combining votes for countries from the day's submissions and the week's (weighed) submissions
    votes = Counter(day.countries) + Counter(week.countries)

    with open('data/votes.json', 'w') as outfile:
        json.dump(votes, outfile)


def news_json(day, week):
    logging.info("Ongoing...")

    # Combining day's submissions and week's into one dictionary
    news = day.headlines

    for key, value in week.headlines.items():
        if key in news.keys():
            news[key] += value
        else:
            news[key] = value

    with open('data/news.json', 'w') as outfile:
        json.dump(news, outfile)


def submissions_json(day, week):
    logging.info("Ongoing...")

    # Combining day's submissions and week's into one dictionary
    submissions = {**day.submissions, **week.submissions}

    with open('data/submissions.json', 'w') as outfile:
        json.dump(submissions, outfile)


def heatedworld():
    logging.info("--------------------")
    logging.info("-------------")
    logging.info("Script starting...\n")

    logging.info("Initiating client for the day's submssions...")
    # subreddit followed by day/week
    redditDay = Reddit("worldnews", "day")
    logging.info("Client initiated.")

    logging.info("Fetching...")
    redditDay.fetch(40)  # 40
    logging.info("Fetched.")

    logging.info("Getting context...")
    redditDay.get_context()
    logging.info("Context saved.")

    logging.info("Getting countries' headlines...")
    redditDay.country_news()
    logging.info("Countries' news saved....")

    logging.info("Saving daily data to CSV and JSON...")
    redditDay.save_csv()
    with open('data/day.json', 'w') as outfile:
        json.dump(redditDay.submissions, outfile)
    logging.info("Saved day's submissions.\n")

    logging.info("----------------------------------------------\n")

    logging.info("Initiating client for the week's submssions...")
    # subreddit followed by day/week
    redditWeek = Reddit("worldnews", "week")
    logging.info("Client initiated.")

    logging.info("Fetching...")
    redditWeek.fetch(120)  # 120
    logging.info("Fetched.")

    logging.info("Getting context...")
    redditWeek.get_context()
    logging.info("Context saved.")

    logging.info("Getting countries' headlines...")
    redditWeek.country_news()
    logging.info("Countries' news saved....")

    logging.info("Saving weekly data to CSV and JSON...")
    redditWeek.save_csv()
    with open('data/week.json', 'w') as outfile:
        json.dump(redditWeek.submissions, outfile)
    logging.info("Saved week's submissions.\n")

    logging.info("----------------------------------------------\n")

    logging.info("Saving heatmap values to JSON file...")
    heatmap_json(redditDay, redditWeek)
    logging.info(("Saved votes JSON file.\n"))

    logging.info("----------------------------------------------\n")

    logging.info("Saving countries' headlines to JSON file...")
    news_json(redditDay, redditWeek)
    logging.info(("Saved news JSON file.\n"))

    logging.info("----------------------------------------------\n")

    logging.info("Saving submissions to JSON file...")
    submissions_json(redditDay, redditWeek)
    logging.info(("Saved submissions JSON file.\n"))

    logging.info("Script finished.")
    logging.info("-------------")
    logging.info("--------------------\n")


logging.basicConfig(filename='data/heatedworld.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if not os.path.exists("data"):
    os.mkdir("data")

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=heatedworld,
    trigger=IntervalTrigger(hours=24),
    next_run_time=datetime.datetime.now(),
    id='getting_elements',
    name='getting elements',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/votes')
def fetch_votes():
    f = open("data/votes.json", "r")
    content = f.read()
    f.close()
    return content


@app.route('/news')
def fetch_country_news():
    f = open("data/news.json", "r")
    content = f.read()
    f.close()
    return content


@app.route('/submissions')
def fetch_submissions():
    f = open("data/submissions.json", "r")
    content = f.read()
    f.close()
    return content


if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)
