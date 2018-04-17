#!/usr/local/bin/python3

#############################################################################
#   Author: Ahmad M. Osman                                                  #
#   Date: 04/10/2018                                                        #
#                                                                           #
#   Project: NewsMaps                                                       #
#   Purpose: World News' Heat Maps.                                         #
#                                                                           #
#                           https://www.newsmaps.xyz                        #
#                  https://github.com/Ahmad-Magdy-Osman/NewsMaps            #
#                                                                           #
#   Filename: script.py                                                     #
#   File functionality: This script executes all the steps to prepare       #
#                       Date to be visualized on NewsMaps.xyz               #
#                                                                           #
#############################################################################

import logging
import json
from reddit import Reddit


def save_json(day, week):
    logging.info("Ongoing...")
    with open('data.json', 'w') as outfile:
        json.dump(day._submissions, outfile)
        json.dump(week._submissions, outfile)


def main():
    logging.basicConfig(filename='script.log', level=logging.INFO,
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

    logging.info("Script finished.")
    logging.info("-------------")
    logging.info("--------------------\n")


if __name__ == "__main__":
    main()
