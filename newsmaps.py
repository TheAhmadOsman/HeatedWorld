#############################################################################
#   Author: Ahmad M. Osman                                                  #
#   Date: 04/17/2018                                                        #
#                                                                           #
#   Project: NewsMaps                                                       #
#   Purpose: World News' Heat Maps.                                         #
#                                                                           #
#                           https://www.newsmaps.xyz                        #
#                  https://github.com/Ahmad-Magdy-Osman/NewsMaps            #
#                                                                           #
#   Filename: newsmaps.py                                                   #
#   File functionality: This file executes all necessary steps to prepare   #
#                       Date to be visualized on NewsMaps.xyz               #
#                                                                           #
#############################################################################

import logging
import time
import json
import requests
import atexit

from flask import Flask, Response, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from reddit import Reddit


app = Flask(__name__)


def save_json(day, week):
    logging.info("Ongoing...")
    with open('data.json', 'w') as outfile:
        json.dump(day._submissions, outfile)
        json.dump(week._submissions, outfile)


def save_json_map(week):
    logging.info("Ongoing...")
    with open('map.json', 'w') as outfile:
        json.dump(week._countries, outfile)


def map_elements():
    logging.basicConfig(filename='newsmaps.log', level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("--------------------")
    logging.info("-------------")
    logging.info("Script starting...\n")

    logging.info("Initiating client for the day's submssions...")
    # subreddit followed by day/week
    redditDay = Reddit("worldnews", "day")
    logging.info("Client initiated.")

    logging.info("Fetching...")
    redditDay.fetch(40)
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
    redditWeek.fetch(100)
    logging.info("Fetched.")

    logging.info("Getting context...")
    redditWeek.get_context()
    logging.info("Context saved.")

    logging.info("Saving data to CSV...")
    redditWeek.save()
    logging.info("Saved week's submissions.\n")

    logging.info("----------------------------------------------\n")

    logging.info("Saving to JSON file...")
    save_json(redditDay, redditWeek)
    logging.info(("Saved JSON file.\n"))

    ###
    save_json_map(redditWeek)

    logging.info("Script finished.")
    logging.info("-------------")
    logging.info("--------------------\n")


map_elements()
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=map_elements,
    trigger=IntervalTrigger(weeks=1),
    id='getting_elements',
    name='getting elements',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def homepage():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
