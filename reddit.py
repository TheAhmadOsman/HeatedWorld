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
#   Filename: reddit.py                                                     #
#   File functionality: Connecting to and fetching news from Reddit         #
#                                                                           #
#############################################################################

import logging
import praw
import csv
import config

# Reddit Client Variables
USERAGENT = ("NewsMaps 1.0 by /u/XMasterrrr" +
             "https://github.com/Ahmad-Magdy-Osman/NewsMaps")
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
        self.redditClient()
        self._submissions = {}
        self._filename = self._subreddit + "_" + self._time + ".csv"

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
    def filename(self):
        return self._filename

    def redditClient(self):
        logging.info("Logging in...")
        self._reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                   password=PASSWORD, user_agent=USERAGENT,
                                   username=USERNAME)
        logging.info("Logged in with: /u/" + str(self._reddit.user.me()))

    def fetch(self, queryLimit):
        logging.info("Ongoing...")
        for submission in self._reddit.subreddit(self._subreddit).top(self._time, limit=queryLimit):
            # print(vars(submission))  # to get a list of the fields of an object
            # We will be saving the following data for up to the queryLimit of the specified time of the specified subreddit
            '''{'title': 'Shell predicted dangers of climate change in 1980s and knew fossil fuel industry was responsible: Authors of confidential documents envisage changes to sea level and weather ‘larger than any that have occurred over the past 12,000 years’.',
            'score': 48748,
            'permalink': '/r/worldnews/comments/8ax9bd/shell_predicted_dangers_of_climate_change_in/',
            'url': 'https://www.independent.co.uk/news/business/news/shell-predicted-climate-change-fossil-fuel-industry-1980s-global-warming-oil-a8294636.html',
            'domain': 'independent.co.uk',
            'created': 1523296387.0,
            'created_utc': 1523267587.0,
            'ups': 48748,
            'num_comments': 2287}'''
            self._submissions[submission.ups] = [submission.title, submission.score, submission.permalink, submission.url,
                                                 submission.domain, submission.created, submission.created_utc, submission.ups, submission.num_comments]

    def save(self):
        logging.info("Ongoing...")
        with open(self._filename, 'w') as csvfile:
            fieldnames = ["title", "score", "permalink", "url", "domain",
                          "created", "created_utc", "ups", "num_comments"]
            out = csv.writer(csvfile, delimiter='\t')
            out.writerow(fieldnames)
            for key, value in self._submissions.items():
                out.writerow(value)
