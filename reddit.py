#############################################################################
#   Author: Ahmad M. Osman                                                  #
#   Date: 04/10/2018                                                        #
#                                                                           #
#   Project: Heated World                                                   #
#   Purpose: World News' Heat Maps.                                         #
#                                                                           #
#                           https://www.heated.world                        #
#                  https://github.com/Ahmad-Magdy-Osman/HeatedWorld         #
#                                                                           #
#   Filename: reddit.py                                                     #
#   File overview: Connecting to and fetching news from Reddit              #
#                                                                           #
#############################################################################

import logging
import csv
import time
import config
import praw

from newspaper import Article
from geotext import GeoText

# Reddit Client Variables
USERAGENT = ("HeatedWorld 1.0 by /u/XMasterrrr" +
             "https://github.com/Ahmad-Magdy-Osman/HeatedWorld")
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD


class Reddit:
    def __init__(self, subreddit, time):
        """Reddit Session

        Arguments:
            subreddit {string} -- subreddit in string
            time {string} -- either day or week
        """

        logging.info("Ongoing...")

        self._subreddit = subreddit
        self._time = time

        # Initiating client
        logging.info("Logging in...")
        self._reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                   password=PASSWORD, user_agent=USERAGENT,
                                   username=USERNAME)
        logging.info("Logged in with: /u/" + str(self._reddit.user.me()))

        # Preparing CSV filename - this file is solely for debugging purposes
        self._filename = self._subreddit + "_" + self._time + ".csv"

        # Dictionary of headlines with their text and geographical analysis
        self._submissions = {}
        # Dictionary for countries along with their votes. These votes will be used to heat the world map.
        self._countries = {}

    @property
    def subreddit(self):
        return self._subreddit

    @subreddit.setter
    def subreddit(self, subreddit):
        self._subreddit = subreddit

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def reddit(self):
        return self._reddit

    @reddit.setter
    def reddit(self, reddit):
        self._reddit = reddit

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def submissions(self):
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        self._submissions = submissions

    @property
    def countries(self):
        return self._countries

    @countries.setter
    def countries(self, countries):
        self._countries = countries

    def fetch(self, queryLimit):
        logging.info("Ongoing...")
        for submission in self._reddit.subreddit(self._subreddit).top(self._time, limit=queryLimit):
            # print(vars(submission))  # to get a list of the fields of an object
            # We will be saving the following data for up to the queryLimit of the specified time of the specified subreddit, in addition to our created fields.
            '''{'title': 'Shell predicted dangers of climate change in 1980s and knew fossil fuel industry was responsible: Authors of confidential documents envisage changes to sea level and weather ‘larger than any that have occurred over the past 12,000 years’.',
            'score': 48748,
            'permalink': '/r/worldnews/comments/8ax9bd/shell_predicted_dangers_of_climate_change_in/',
            'url': 'https://www.independent.co.uk/news/business/news/shell-predicted-climate-change-fossil-fuel-industry-1980s-global-warming-oil-a8294636.html',
            'domain': 'independent.co.uk',
            'created': 1523296387.0,
            'created_utc': 1523267587.0,
            'ups': 48748,
            'num_comments': 2287}'''

            if self._time == "week":
                submission_days = (
                    (time.time() - (submission.created_utc - 60*61)) // (24*60*60)) + 1
                # Removing duplicates between "day" and "week" headlines
                if submission_days == 1:
                    continue
                # Calculating score for each headline based on 1-(n/7).
                elif submission_days > 7:
                    submission_days = 7
                    calculated_score = int(submission.score * 1/7)
                elif submission_days > 1 and submission_days < 7:
                    calculated_score = int(
                        submission.score * (1 - (submission_days/7)))
                else:
                    calculated_score = submission.score
            elif self._time == "day":
                submission_days = 1
                calculated_score = submission.score
            else:
                return None

            self._submissions[calculated_score] = {"calculated_score": calculated_score, "submission.score": submission.score, "submission.title": submission.title, "submission_days": submission_days, "submission.permalink": (
                "https: // www.reddit.com /" + submission.permalink), "submission.url": submission.url, "submission.domain": submission.domain, "submission.created_utc": submission.created_utc, "submission.num_comments": submission.num_comments}

    def get_context(self):
        logging.info("Ongoing...")
        for value in self._submissions.values():
            try:
                article = Article(value["submission.url"])
                article.download()
                article.parse()
                article.nlp()
                value["article.authors"] = article.authors
                value["article.text"] = article.text

                places = GeoText(article.text)
                for country in set(places.countries):
                    if not str(country) in self._countries:
                        self._countries[str(
                            country)] = value["calculated_score"]
                    else:
                        self._countries[str(
                            country)] += value["calculated_score"]

                value["article.top_image"] = article.top_image
                value["article.summary"] = article.summary
                value["article.keywords"] = article.keywords
                value["article.countries"] = places.countries
            except Exception as e:
                logging.info("Error: " + str(e))

    def save(self):
        logging.info("Ongoing...")
        with open(self._filename, 'w') as csvfile:
            fieldnames = ["calculated_score", "submission.score", "submission.title", "submission_days", "submission.permalink", "submission.url", "submission.domain",
                          "submission.created_utc", "submission.num_comments", "article.authors", "article.text", "article.top_image", "article.summary", "article.keywords", "article.countries"]
            out = csv.writer(csvfile, delimiter='\t')
            out.writerow(fieldnames)
            for value in self._submissions.values():
                out.writerow(value.values())
