# NewsMaps - https://www.newsmaps.xyz
* Fetching news from Reddit; /r/worldnews
  * https://www.reddit.com/dev/api/
  * Top 80 articles in the last 24 hours
  * Top 80 articles in the last 7 days
* Getting news headline, description, and source location
  * https://newsapi.org
* Extracting geographical info
  * https://github.com/Corollarium/geograpy2
* Creating world heatmap
  * https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap
  * http://datamaps.github.io/
  * Heatmap depends on Reddit's post date(on scale of 1-7) + the number of votes. Past 24 hours news should create the initial heatmap first based on votes, and from their a ratio can be taken for the amount of heat the older news will get.
* Creating submaps for each country, with headlines and links to articles and reddit discusions
  * Again, this should be a heatmap based on the previously stated logic.
* DigitalOcean Hosting
