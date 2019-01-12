# :world_map: Heated World :newspaper:

Heated World is the news aggregator you've always needed but never knew you do. This web app, simply put, fetches the top 160 upvoted headlines from Reddit, parses the articles, extract countries from said articles, does NLP summarization of the articles, do some weighing calculations, and then heat an interactive world map based on the weighted values for each headline. The heat map is interactive showing you articles per country with their thumbnails, summaries, and reddit discussion stats and links, all ordered by the weigh of their importance and their relative date to today. In short, Heated World is an Interactive Live World News Heat Map with Natural Language Processing, Summaries, and Reddit Discussions :sunglasses:.

One of the reasons I love [Reddit](https://www.reddit.com/) is that it feels like a place for everybody – a place for the citizens of the world. It is amusing, and at the same time very informative. Over the past few years I have drifted away from Facebook and its alike to Reddit. I spend most of free my time on it, either surfing my feed or visiting subreddits of my interest. Millions browse Reddit everyday, either to submit new content to their favorite subreddits, or to contribute in discussions and/or upvote content. This, for me, is a form of natural selection. Good, important, and interesting content live by getting upvoted and being discussed, causing that content to trend, while the useless content gets lost in the process. The [World News](https://www.reddit.com/r/worldnews/) subreddit is a great example of a subreddit that I am always browsing. I first knew of the Facebook–Cambridge Analytica data scandal via that subreddit, and I believe that it was one of the accelerators that caused the spread of information about said scandel. In my view, the World News subreddit is one of the most important news aggregators ever. It is filtered by humans for humans, not just as in how many times a headline was visited, but rather as in how many times has it been upvoted and how many comments and discussions does it have. 

With that in mind, I am more of a visual person, and having the news visualized on the World Map, telling me where are the news and what places are heated, and being able to locate news by clicking on countries, seemed like something I am always missing. Besides that, I usually do not have time to read the articles beyond just the headlines, so also a way to summarize article contents seemed crucial. From there, I decided to start Heated World, The World News Aggregator That You Always Needed, to fill in the gaps for all those missing features I have always needed.

## Table of Content :blue_book:	

   * [<g-emoji class="g-emoji" alias="world_map" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f5fa.png">🗺️</g-emoji> Heated World <g-emoji class="g-emoji" alias="newspaper" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4f0.png">📰</g-emoji>](#world_map-heated-world-newspaper)
      * [Table of Content <g-emoji class="g-emoji" alias="blue_book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d8.png">📘</g-emoji>](#table-of-content-blue_book)
      * [Features <g-emoji class="g-emoji" alias="sparkles" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2728.png">✨</g-emoji> <g-emoji class="g-emoji" alias="sunglasses" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f60e.png">😎</g-emoji>](#features-sparkles-sunglasses)
      * [Demo and Screenshots <g-emoji class="g-emoji" alias="camera" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4f7.png">📷</g-emoji> <g-emoji class="g-emoji" alias="video_camera" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4f9.png">📹</g-emoji>](#camera-demo-and-screenshots-video_camera)
      * [Usage <g-emoji class="g-emoji" alias="video_game" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3ae.png">🎮</g-emoji>](#usage-video_game)
        * [Cloning and Virtual Environment](#cloning-and-virtual-environment)
        * [Running Mordecai Prerequisites](#running-mordecai-prerequisites)
        * [Reddit API Credentials](#reddit-api-credentials)
        * [Running the Web App](#running-the-web-app)
      * [Tools <g-emoji class="g-emoji" alias="eyeglasses" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f453.png">👓</g-emoji>](#tools-eyeglasses)
      * [Current Web App Hierarchy <g-emoji class="g-emoji" alias="muscle" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4aa.png">💪</g-emoji>](#current-web-app-hierarchy-muscle)
      * [Future Plans <g-emoji class="g-emoji" alias="soon" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f51c.png">🔜</g-emoji>](#future-plans-soon)
      * [Contributing <g-emoji class="g-emoji" alias="fire" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f525.png">🔥</g-emoji>](#contributing-fire)
      * [Collaborators & Contributors <g-emoji class="g-emoji" alias="man_dancing" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f57a.png">🕺</g-emoji> <g-emoji class="g-emoji" alias="dancer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f483.png">💃</g-emoji>](#man_dancing-collaborators--contributors-dancer)
      * [Inspiration <g-emoji class="g-emoji" alias="notebook" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d3.png">📓</g-emoji>](#inspiration-notebook)
      * [License <g-emoji class="g-emoji" alias="books" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4da.png">📚</g-emoji>](#license-books)

## Features :sparkles: :sunglasses:

Currently, Heated World supports the following:

* Fetching Headlines from Reddit's r/WorldNews
  * Top 40 articles in the last 24 hours
  * Top 120 articles in the last 7 days
  * Number of articles for both categories can be changed in heatedworld.py within the fetch function argument.
* Downloading Headlines' Articles and Summarizes them.
* Extracting Geographical Context
  * Leverages Elastic Search in Finding Countries from the Articles' Content.
* Build multipe CSV and JSON files while processing the data.
  * Build Countries Map with Related Headlines and Calculated Weighing Values.
* Building Heat Map

## :camera: Demo and Screenshots :video_camera:

Heated World                           | Heated World
:-------------------------:|:-------------------------:
![Landing Page](img/readme/1-Landing.png)   |  ![Register](img/readme/2-Register.png)
![Invalid Register](img/readme/3-RegisterFailure.png)  |  ![Paths](img/readme/4-Login.png)
![Mainpage](img/readme/5-Mainpage.png)  |  ![Searching](img/readme/6-Searching.png)

![Movie](img/readme/7-Movie.png)

![Demo](img/readme/Demo.gif)

## Usage :video_game:

This web app is written in **Python 3.6** using **Flask** Web Framework. Heat Map is generated using **JS**, **D3.js**, and Datamaps. Frontend uses **Bootstrap** Framework. **Docker** and **Elasticsearch** are used to extract Geographical context - you will need, as instructed below, to have Geonames gazetteer running in Elasticsearch for [Mordecai](https://github.com/openeventdata/mordecai#installation-and-requirements) to be able to successfully extract geographical context. **JSON** and **CSV** data formats are used, too.

### Cloning and Virtual Environment

Make sure you have **Python 3.6** installed.

* `git clone https://github.com/Ahmad-Magdy-Osman/HeatedWorld.git`
* `cd HeatedWorld`
* `python3.6 -m venv venv`
* `source venv/bin/active`
* You might want to update pip using `python-3.6 -m pip --upgrade pip`
* Install requirements with `python3.6 -m pip install -r requirements.txt`

### Running Mordecai Prerequisites

This step is essential before running the web app.

* Install [Docker](https://docs.docker.com/install/) and [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
* Download the required spaCy NLP model using `python3.6 -m spacy download en_core_web_lg`
* `mkdir others`
* `cd others`
* `docker pull elasticsearch:5.5.2`
* `wget https://s3.amazonaws.com/ahalterman-geo/geonames_index.tar.gz --output-file=wget_log.txt`
* `tar -xzf geonames_index.tar.gz`
* `docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2`

### Reddit API Credentials

This step is essential before running the web app. You will need an account on Reddit and you will need to create an app token.

* `touch config.py`
* Inside config.py, the follow lines should reside with your acquired credentials:
  ```
  CLIENT_ID = "Reddit Generated Client ID"
  CLIENT_SECRET = "Reddit Generated Client Secret"
  USERNAME = "Reddit Username"
  PASSWORD = "Reddit Password"
  ```

### Running the Web App

The Web App is scheduled to fetch 120 articles from the weekly top posts and 40 from the daily top posts. It then processes the data using several algorithms and does NLP. I recommend changing the number of headlines to fetch to 4-8 headlines or something like that while testing the web app - this can be done in heatedworld.py within the fetch function argument.

* Make sure a folder called data is in place `mkdir data`
* Run the Web App using `python3.6 heatedworld.py`
  * This will take some time, the NLP to find accurate countries from the articles takes a lot of time. There is a file called heatedworld.log within the data folder where you can see that the application is processing data.
* Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Tools :eyeglasses:

Programming Languages, Frameworks, Libraries, APIs, Databases, and Data Formats.

* Python 3
  * Flask
    * Flask-WTF
    * Flask-Bootstrap
  * Reddit: [PRAW](https://github.com/praw-dev/praw)
  * Natural Language Processing: [Newspaper3k](https://github.com/codelucas/newspaper)
  * Geographical Context: [Mordecai](https://github.com/openeventdata/mordecai)
* Javascript
  * D3.js
  * [Datamaps](http://datamaps.github.io/)
* HTML & CSS
  * Bootstrap Framework
* JSON & CSV Data Formats

## Current Web App Hierarchy :muscle:

* Main Page
  * Heat Map
  * Multiple Sections
* Clickable Heatmap Regions
  * Headlines, Summaries, and Reddit Discussions
* More to come...

## Future Plans :soon:

Some of the features and functions that would be appropriate for Heated World. Please feel free to pick any of them and start working on improving it as a contributor. The target of Heated World is to become an essential part of the Reddit News world.

* General
  * Mobile Responsiveness
  * Project Structure and Cleaning
  * Changing Heat Colors & Gradients
* Features
  * Combining Similar Articles.
  * Words Cloud
    * Clickable with all related articles.
  * Comment, upvote, and discussions directly from Heated World.
    * Will require singing in with Reddit account.
  * News List Per Country
    * Dropdown to choose country and all news are in-front of you.
* Style/Design
  * Fonts
  * GitHub Corner
  * Divs & Footer
* Database
  * Use PostgreSQL instead of CSV
    * Tables - many-to-many relationships
      * Countries, Articles, Articles Daily, and Articles Weekly
    * JSON files are built from the DB after fetching from Reddit and after getting articles summaries and geographical context.
* Back End
  * Multi-threading
    * Concurrent connections to the PostgreSQL DB before Articles Processing and Context Extraction.
  * Processing in Batches.
    * Get all values in a list, loop through them in orders of 10s, and get contexts for each ten by calling their primary key.
  * Fetching from Reddit
    * If in DB
      * Update number of upvotes and recalculate the weight.
      * Updates number of votes for countries table too
      * If it is in weekly top voted headlines, should be just moved from daily and number of upvotes and calculated weight get updated.
        * If it was not on daily, continue.
      * Skip the next two steps for this case
    * Remove all headlines the are neither part of the daily nor the weekly top posts of the given range.
    * Make sure no duplicates exist between daily and weekly tables.
  * Articles Processing
    * Use multi-threading and batches method described above.
    * Each article is directly saved to DB and not kept in memory.
    * Extract Context
  * Geographical Context Extraction
    * Use multi-threading and batches method described above.
    * Checks if the same article - using the article link as primary key is in the DB, if so, skip.
    * Removing the most popular 10k words from the text before using Mordecai.
      * Maybe find strange words and do geographical context extraction on that?
* Marketing
  * SEO
  * Product Hunt
    * Product Hunt Upvote Button
  * Share on Social Media Buttons
* Live Version
  * Frontend Revamp
  * Back End Rewriting
    * A rewriting is ongoing in branch `rewriting`
* Read Me
  * Add Collaborates and Contributors

## Contributing :fire:

1. :spaghetti: Fork this repo!
2. Clone and `cd` into it
3. Setup your virtual environment.
4. Create your feature branch: `git checkout -b my-new-feature`
5. Commit your changes: `git commit -m 'Add some feature'`
6. Push to the branch: `git push origin my-new-feature`
7. Submit a pull request :+1:

## :man_dancing: Collaborators & Contributors :dancer:

[<img src="https://github.com/Ahmad-Magdy-Osman.png" width="114px;"/><br /><sub><b>Ahmad M. Osman</b></sub>](https://github.com/Ahmad-Magdy-Osman)<br />

## Inspiration :notebook:

> **You will fail.**
> 
> You will mess up.
> 
> You'll do poorly on assignments and tests.
> 
> Your side projects will not work.
> 
> Your code will be sloppy and incomplete.
> 
> You will bomb job interviews.
> 
> Your PR's will be rejected.
> 
> And because you fail, you will succeed.
> 
> Don't be afraid to fail, don't let it destroy your self-confidence, don't let it define you. Instead, do everything you can to learn from that failure and take that new knowledge into the next piece of work.
> 
> Indeed, failure is the only path to success.

        ― Stranger on the Internet.

## License :books:

Heated World is an open source project under MIT license.
