// Generating the heated world map and fetching news headlines for each country.
function map() {
    // Countries alongside their number of votes and selected filling colors.
    let dataSet = {};
    // Votes values for statistical calculations
    let values = [];

    // Reading number of votes from its app route
    readJSON("/votes");
    // Reading the headlines for each country from its app route
    readJSON("/news");

    // Starting statistical calculations
    var valueDict = JSON.parse(localStorage.getItem("/votes"));

    // Fetching values to determine min/max
    for (let item in valueDict) {
        values.push(valueDict[item]);
    }

    var minValue = Math.min(...values);
    var maxValue = Math.max(...values);

    // Deciding min and max colors
    var minColor = "#FFFFB2";
    var maxColor = "#80001a";

    /* Using d3 scale module to build a scale between minColor and maxColor based on the min and max number of upvotes */
    var colorScale = d3
        .scale
        .linear()
        .domain([minValue, maxValue])
        .range([minColor, maxColor]);

    // Statistical calculations for colors
    var halfWay = Median(values);
    var two = Quartile_25(values);
    var four = Quartile_75(values);

    //Fetch country/value and popluate the dataSet
    var fills = {};
    for (let item in valueDict) {
        let country = item;
        let val = valueDict[item];
        dataSet[country] = {
            "fillColor": colorScale(val),
            "numberOfVotes": val
        };
    }

    //generate a map
    var map = new Datamap({
        element: document.getElementById("map"),
        responisve: true,
        fills: {
            defaultFill: "#ffffe6",
            minValue: "#FFFFB2",
            two: "#DE806C",
            halfWay: "#CE4049",
            four: "#BD0026",
            maxValue: "#80001a"
        },
        data: dataSet,
        projection: "mercator",
        geographyConfig: {
            highlightFillColor: '#565656',
            highlightBorderColor: '#444',
            borderColor: '#444',
            borderWidth: 0.5,
            popupTemplate: function (geo, data) {
                return [
                    '<div class="hoverinfo"><strong>', 'Number of people discussing ' + geo.properties.name,
                    ': ' + data.numberOfVotes,
                    '</strong></div>'
                ].join('');
            }
        },
        done: function (datamap) {
            datamap
                .svg
                .selectAll('.datamaps-subunit')
                .on('click', function (geography) {
                    let fullCountry = geography.properties.name;
                    let popup = document.getElementById("popup");
                    let close = document.getElementById("close");
                    let closebtn = document.getElementById("closebtn");
                    popup.style.display = "block";
                    close.onclick = function () {
                        popup.style.display = "none";
                    };
                    closebtn.onclick = function () {
                        popup.style.display = "none";
                    };
                    window.onclick = function (event) {
                        if (event.target == popup) {
                            popup.style.display == "none"; // jshint ignore:line
                        }
                    };
                    let popupHead = document.getElementById("popupHead");
                    let popupBody = document.getElementById("popupBody");
                    let popupFoot = document.getElementById("popupFoot");
                    popupHead.innerHTML = "News from " + fullCountry;
                    popupHead.style.textAlign = "left";
                    //building the data dictionary from localStorage
                    var dataDict = JSON.parse(localStorage.getItem("/news"));
                    popupString = "";
                    var countryDict = dataDict[geography.id];
                    if (!Array.isArray(countryDict) || !countryDict.length) {
                        popupString = '<h3 class="text-center">Looks like ' + fullCountry + ' does not have any trending news for now!</h3>';
                    }
                    for (var article in countryDict) {
                        let score = countryDict[article]["submission.score"];
                        let title = countryDict[article]["submission.title"];
                        let link = countryDict[article]["submission.url"];
                        let website = countryDict[article]["submission.domain"]
                        let comments = countryDict[article]["submission.num_comments"];
                        let reddit = countryDict[article]["submission.permalink"];
                        let photo = countryDict[article]["article.top_image"];
                        let summary = countryDict[article]["article.summary"];

                        popupString = popupString + '<div class="jumbotron"><div class="grid-container"><div data-area="article_image' +
                                '"><img src="' + photo + '" alt="Article Image" style="width:400px;height:400px;border-radius: 25px;"></di' +
                                'v><div data-area="reddit_info" class="text-center"><br>Number of Reddit Upvotes:' +
                                ' ' + score + '. </br> Number of Reddit Comments : ' + comments + '. </div><div data-area="reddit_links"><a target="_blank" href="' + reddit + '"><br><h5 class="text-center">Reddit Discussion</h5></a></div><div data-area="ar' +
                                'ticle_summary"><p align="justify">' + summary + '</p></div><div data-area="article_headline"><a target="_blank" href="' + link + '"><h3 class="text-center"><br><br>' + title + '</h3></a></div></div></div><hr>';
                    }
                    popupBody.innerHTML = popupString;
                    /*
                        <div class="grid-container">
                            <div data-area="article_image">
                                article_image
                            </div>
                            <div data-area="reddit_info">
                                reddit_info
                            </div>
                            <div data-area="reddit_links">
                                reddit_links
                            </div>
                            <div data-area="article_summary">
                                article_summary
                            </div>
                            <div data-area="article_headline">
                                article_headline
                            </div>
                        </div>
                    */
                });
        }
    });

    /* map.legend({
        labels: {
            minValue: minValue,
            two: two,
            halfWay: halfWay,
            four: four,
            maxValue: maxValue
        }
    }); */

    window.addEventListener('resize', function () {
        map.resize();
    });
}