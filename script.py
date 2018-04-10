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
from reddit import Reddit


def main():
    logging.basicConfig(filename='script.log', level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("--------------------")
    logging.info("-------------\n")
    logging.info("Script starting...")
    logging.info("Initiating client...")
    # subreddit followed by day/week
    reddit = Reddit("worldnews", "week")
    logging.info("Client initiated.")
    logging.info("Fetching...")
    reddit.fetch(100)
    logging.info("Fetched.")
    logging.info("Saving data to CSV...")
    reddit.save()
    logging.info("Saved.")
    logging.info("Script finished.\n")
    logging.info("-------------")
    logging.info("--------------------\n")


if __name__ == "__main__":
    main()
