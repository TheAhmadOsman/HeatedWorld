import logging
import csv
import time
import config
import praw
import os
from newspaper import Article
from mordecai import Geoparser

logging.basicConfig(filename='data/heatedworld.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

REDDIT = None
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
USERAGENT = ("HeatedWorld 1.0 by /u/XMasterrrr" +
             "https://github.com/Ahmad-Magdy-Osman/HeatedWorld")


def login():
    '''Reddit Login'''
    logging.info("Ongoing...")

    global REDDIT

    # Initiating client
    logging.info("Logging in...")
    REDDIT = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         password=PASSWORD, user_agent=USERAGENT,
                         username=USERNAME)
    logging.info("Logged in with: /u/" + str(REDDIT.user.me()))


def fetch(subreddit, timewindow, queryLimit):
    '''Fetching submissions from and calculating submission score Reddit'''
    if timewindow not in ["day", "week"]:
        logging.info(
            f"Error...\nIncorrect time window: {timewindow}\nAborted.")
        raise ValueError()

    logging.info("Ongoing...")

    submitted = REDDIT.subreddit(subreddit).top(timewindow, limit=queryLimit)
    submissions = {}

    for submission in submitted:
        # print(vars(submission))  # to get a list of the fields of an object
        '''
            We will be saving the following data for up to the queryLimit of the specified time of the specified subreddit, in addition to our created fields:
                'title': 'Shell predicted dangers of',
                'score': 48748,
                'permalink': '/r/worldnews/comments/8ax9bd/shell_predicted_dangers_of_climate_change_in/',
                'url': 'https://www.independent.co.uk/news/business/news/shell-predicted-climate-change-fossil-fuel-industry-1980s-global-warming-oil-a8294636.html',
                'domain': 'independent.co.uk',
                'created': 1523296387.0,
                'created_utc': 1523267587.0,
                'ups': 48748,
                'num_comments': 2287
        '''

        # If weekly, we calculate the submission vote score
        if timewindow == "week":
            submission_days = (
                (time.time() - (submission.created_utc - 60*61)) // (24*60*60)) + 1
            # Removing duplicates between "day" and "week" headlines
            if submission_days == 1:
                continue
            # Calculating score for each headline based on 1-(n/7).
            elif submission_days > 7:
                submission_days = 7
                calculated_score = int(submission.score * 1/7)
            elif 1 < submission_days < 7:
                calculated_score = int(
                    submission.score * (1 - (submission_days/7)))
            else:
                calculated_score = int(submission.score * 1/7)
        elif timewindow == "day":
            submission_days = 1
            calculated_score = submission.score
        else:
            return None

        submissions[calculated_score] = {"calculated_score": calculated_score, "submission.score": submission.score, "submission.title": submission.title, "submission_days": submission_days, "submission.permalink": str(
            "https: // www.reddit.com /" + submission.permalink).replace(" ", ""), "submission.url": submission.url.replace(" ", ""), "submission.domain": submission.domain, "submission.created_utc": submission.created_utc, "submission.num_comments": submission.num_comments}
    return submissions


COUNTRIES = {}

words = None
with open("./words/words.txt") as f:
    words = f.readlines()
    words = [x.strip() for x in words]
words = set(words)


def get_context(submission):
    '''Getting Submissions Context'''
    logging.info("Ongoing...")

    global COUNTRIES

    try:
        article = Article(submission["submission.url"])
        article.download()
        article.parse()
        article.nlp()
        submission["article.authors"] = article.authors
        submission["article.text"] = article.text

        splitted = article.text.split()
        splitted = [x.strip() for x in splitted]
        splitted = set(splitted)
        global words
        diff = splitted - words
        diff = ' '.join(diff)
        print(diff)

        geo = Geoparser()
        places = geo.geoparse(diff)

        countries_in_article = set()

        for country in places:
            countries_in_article.add(country["country_predicted"])

        for country in countries_in_article:
            if not str(country) in COUNTRIES:
                COUNTRIES[str(
                    country)] = submission["calculated_score"]
            else:
                COUNTRIES[str(
                    country)] += submission["calculated_score"]

        submission["article.top_image"] = article.top_image
        submission["article.summary"] = article.summary
        submission["article.keywords"] = article.keywords
        submission["article.countries"] = list(countries_in_article)
        print(submission)
        return submission
    except Exception as e:
        logging.info("Error: " + str(e))


def main():
    login()
    now = time.time()
    submissions = fetch("worldnews", "week", 20)
    filename = "test.csv"

    with open(str("data/" + filename), 'w') as csvfile:
        fieldnames = ["calculated_score", "submission.score", "submission.title", "submission_days", "submission.permalink", "submission.url", "submission.domain",
                      "submission.created_utc", "submission.num_comments", "article.authors", "article.text", "article.top_image", "article.summary", "article.keywords", "article.countries"]
        out = csv.writer(csvfile, delimiter='\t')
        out.writerow(fieldnames)
        count = 0
        for submission in submissions:
            count += 1
            print(count)
            new = get_context(submissions[submission])
            try:
                out.writerow(new.values())
            except:
                print("EXCEPTION!!!")

    now2 = time.time() - now
    print(now2)
    global COUNTRIES
    # print(COUNTRIES)


if __name__ == "__main__":
    main()

#     def country_news(self):
#         logging.info("Ongoing....")
#         for value in self._submissions.values():
#             value_dict = {"submission.score": value["submission.score"], "submission.title": value["submission.title"], "submission.permalink": value["submission.permalink"], "submission.url": value["submission.url"],
#                           "submission.domain": value["submission.domain"], "submission.num_comments": value["submission.num_comments"], "article.top_image": value["article.top_image"], "article.summary": value["article.summary"]}
#             for country in value["article.countries"]:
#                 if not str(country) in self._headlines:
#                     self._headlines[str(country)] = []
#                 self._headlines[str(country)].append(value_dict)


# TODO:
'''
    Dictionary for Old Submissions, Remove the outdated ones from Each Kind, Use JSON
        If exists, update number of votes - updates votes for countries too
    Weekly should be copied from daily and then update votes
    Batches
        Get all values in a list, loop through them in orders of 10s, and get contexts for each ten by calling their dictionary value
    Multithreaded
    ML Concurrently on Unfound Ones only - Maybe find strange words and do ML on that
        Yup, remove top 1000 words or so!
    Words Cloud -> Clickable with all the articles related. Top 50?
    The target of Heated World is to become the Reddit of News... Inspiration of France's recent protests.
    Heated World can combine similar articles.
    Live machine learning
    Product Hunt - GitHub Corner - Share Links & Upvote Product Hunt
    Sign in with Reddit - comments and discussion directly under the website.
'''
