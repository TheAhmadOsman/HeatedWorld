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
#                       Date to be visualized on Heated.World               #
#                                                                           #
#############################################################################

import logging
import time
import json
import requests
import atexit
import os
from collections import Counter
from flask import Flask, Response, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from reddit import Reddit


app = Flask(__name__)


def submissions_json(day, week):
    logging.info("Ongoing...")

    # Combining day's submissions and week's into one dictionary
    submissions = {**day.submissions, **week.submissions}

    with open('data/submissions.json', 'w') as outfile:
        json.dump(submissions, outfile)


def heatmap_json(day, week):
    logging.info("Ongoing...")

    # Combining votes for countries from the day's submissions and the week's (weighed) submissions
    votes = Counter(day.countries) + Counter(week.countries)

    with open('data/mapvotes.json', 'w') as outfile:
        json.dump(votes, outfile)


def heatedworld():
    logging.basicConfig(filename='data/heatedworld.log', level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("--------------------")
    logging.info("-------------")
    logging.info("Script starting...\n")

    logging.info("Initiating client for the day's submssions...")
    # subreddit followed by day/week
    redditDay = Reddit("worldnews", "day")
    logging.info("Client initiated.")

    logging.info("Fetching...")
    redditDay.fetch(50)
    logging.info("Fetched.")

    logging.info("Getting context...")
    redditDay.get_context()
    logging.info("Context saved.")

    logging.info("Saving data to CSV...")
    redditDay.save()
    logging.info("Saved day's submissions.\n")

    logging.info("----------------------------------------------\n")

    logging.info("Initiating client for the week's submssions...")
    # subreddit followed by day/week
    redditWeek = Reddit("worldnews", "week")
    logging.info("Client initiated.")

    logging.info("Fetching...")
    redditWeek.fetch(120)
    logging.info("Fetched.")

    logging.info("Getting context...")
    redditWeek.get_context()
    logging.info("Context saved.")

    logging.info("Saving data to CSV...")
    redditWeek.save()
    logging.info("Saved week's submissions.\n")

    logging.info("----------------------------------------------\n")

    logging.info("Saving submissions to JSON file...")
    submissions_json(redditDay, redditWeek)
    logging.info(("Saved Submissions JSON file.\n"))

    logging.info("----------------------------------------------\n")

    logging.info("Saving heatmap values to JSON file...")
    heatmap_json(redditDay, redditWeek)
    logging.info(("Saved heatmap JSON file.\n"))

    logging.info("Script finished.")
    logging.info("-------------")
    logging.info("--------------------\n")


if not os.path.exists("data"):
    os.mkdir("data")
heatedworld()
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=heatedworld,
    trigger=IntervalTrigger(hours=1),
    id='getting_elements',
    name='getting elements',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/data')
def fetchData():
    f = open("data/submissions.json", "r")
    content = f.read()
    f.close()
    return content


@app.route('/map')
def fetchMap():
    f = open("data/mapvotes.json", "r")
    content = f.read()
    f.close()
    return content


if __name__ == '__main__':
    app.run(debug=True, port=5001)
