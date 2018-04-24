//example data copied from server
function map() {

    // expected arrangment: {"countryName": {"fillColor": #colorcode,
    // "numberOfWhatever": num}}
    let dataSet = {}

    let values = []

    readJSON("/map")
    readJSON("/data")

    var valueDict = JSON.parse(localStorage.getItem("/map"))

    //fetching values to determine min/max
    for (let item in valueDict) {
        values.push(valueDict[item])
    }

    var minValue = Math.min(...values)
    var maxValue = Math.max(...values)

    var minColor = "#FFFFB2"
    var maxColor = "#BD0026"

    // using d3 scale module to build a scale between dark green (light) and dark
    // red (heavy)
    var colorScale = d3
        .scale
        .linear()
        .domain([minValue, maxValue])
        .range([minColor, maxColor])

    var halfWay = Math.round((maxValue - minValue) * .5)
    var two = Math.round((maxValue - minValue) * .25)
    var four = Math.round((maxValue - minValue) * .75)

    //fetch country/value and popluate the dataSet
    var fills = {}
    for (let item in valueDict) {
        let country = item
        let val = valueDict[item]
        if (country == "United States of America") {
            country = "United States"
        }
        dataSet[getIsoThree(country)] = {
            "fillColor": colorScale(val),
            "numberOfWhatever": val
        }
    }
    for (let item in isoCountries) {
        if (getIsoThree(item) in dataSet) {} else {
            dataSet[getIsoThree(item)] = {
                "fillColor": minColor,
                "numberOfWhatever": 0
            }
        }
    }

    //generate a map
    var map = new Datamap({
        element: document.getElementById("map"),
        responisve: true,
        fills: {
            defaultFill: "FFFFB2",
            minValue: "#FFFFB2",
            two: "#EFBF8F",
            halfWay: "#DE806C",
            four: "#CE4049",
            maxValue: "BD0026"
        },
        // fills: {defaultFill: "FFFFB2", minValue: "#FFFFB2", two: "#EFC08F", halfWay:
        // "#DE806C", four: "#CE4049", maxValue: "BD0026"},

        /* fills: {defaultFill: "white", minValue: "#FFFFB2", two: "#EFC08F", halfWay: "#DE806C", four: "#CE4049", maxValue: "BD0026"},*/

        data: dataSet,
        projection: "mercator",
        geographyConfig: {
            highlightFillColor: '#565656',
            borderColor: '#444',
            borderWidth: 0.5,
            popupTemplate: function (geo, data) {
                return [
                    '<div class="hoverinfo"><strong>', 'Number of upvotes in ' + geo.properties.name,
                    ': ' + data.numberOfWhatever,
                    '</strong></div>'
                ].join('');
            }
        },
        done: function (datamap) {
            datamap
                .svg
                .selectAll('.datamaps-subunit')
                .on('click', function (geography) {
                    //triggered by clicking on a country
                    /*                    let link = "popup.html#"
                          link = link + geography.properties.name
                          window.open(link, "_blank");*/
                    let fullCountry = geography.properties.name
                    let iso = getIsoThree(fullCountry)
                    let popup = document.getElementById("popup")
                    let close = document.getElementById("close")
                    popup.style.display = "block"
                    close.onclick = function () {
                        popup.style.display = "none"
                    }
                    window.onclick = function (event) {
                        if (event.target == popup) {
                            popup.style.display == "none"
                        }
                    }
                    let popupHead = document.getElementById("popupHead")
                    let popupBody = document.getElementById("popupBody")
                    let popupFoot = document.getElementById("popupFoot")
                    popupHead.innerHTML = "News from " + fullCountry
                    //building the data dictionary from localStorage
                    var dataDict = JSON.parse(localStorage.getItem("/data"))
                    console.log(dataDict)
                    popupString = ""
                    var countryDict = dataDict[fullCountry]
                    for (article in countryDict) {
                        let title = countryDict["submission.title"]
                        let link = countryDict["submission.url"]
                        let score = countryDict["submission.score"]
                        let comments = countryDict["submission.num_comments"]
                        //Spaces in reddit
                        let reddit = countryDict["submission.permalink"]
                        let photo = "https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1440,w_" +
                                "2560,x_0,y_0/dpr_2.0/c_limit,w_740/fl_lossy,q_auto/v1491846321/cheats/2017/02/02" +
                                "/matthew-mcconaughey-time-to-embrace-trump/170202-mcconaughey-trump-bbc-cheat_df" +
                                "ukwc"
                        popupString = popupString + "<h5><b><a href=" + link + " target=_blank>" + title + "</a></b></h5><p><a href=" + reddit + " target=_blank> Number of comments: " + comments + "</a></p><p><a href=" + reddit + " target=_blank> Number of likes: " + score + "</a></p><img src=" + photo + " alt=Photo </img>"
                    }
                    popupBody.innerHTML = popupString;

                });
        }
    })
    map.legend({
        labels: {
            minValue: minValue,
            two: two,
            halfWay: halfWay,
            four: four,
            maxValue: maxValue
        }
    })

    window.addEventListener('resize', function () {
        map.resize();
    });
}