//example data copied from server
function map(){


        //expected arrangment: {"countryName": {"fillColor": #colorcode, "numberOfWhatever": num}}
        let dataSet = {}

        let values = []

        //fetching values to determine min/max
        for (let item in valueDict){
          values.push(valueDict[item])
        }

        var minValue = Math.min(...values)
        var maxValue = Math.max(...values)

        //using d3 scale module to build a scale between dark green (light) and dark red (heavy)
        var colorScale = d3.scale.linear()
          .domain([minValue, maxValue])
          .range(["#FFFFB2","#BD0026"])

        var halfWay = Math.round((maxValue - minValue) * .5)
        var two = Math.round((maxValue - minValue) * .25)
        var four = Math.round((maxValue - minValue) * .75)

        //fetch country/value and popluate the dataSet
        var fills = {}
        for (let item in valueDict){
          let country = item
          let val = valueDict[item]
          if (country == "United States of America"){
            country = "United States"
          }
          dataSet[getIsoThree(country)] = {"fillColor": colorScale(val), "numberOfWhatever": val}
        }
/*        for (let item in isoCountries){
          if (item in key){
            console.log(item)
          }
        }*/

        //generate a map
        var map =  new Datamap({
          element: document.getElementById("map"),
          responisve : true,
          fills: {defaultFill: "FFFFB2", minValue: "#FFFFB2", two: "#EFBF8F", halfWay: "#DE806C", four: "#CE4049", maxValue: "BD0026"},
          //fills: {defaultFill: "FFFFB2", minValue: "#FFFFB2", two: "#EFC08F", halfWay: "#DE806C", four: "#CE4049", maxValue: "BD0026"},
          data: dataSet,
          projection: "mercator",
          geographyConfig: {
            highlightFillColor: '#565656',
            borderColor: '#444',
            borderWidth: 0.5,
            popupTemplate: function(geo, data){
                return ['<div class="hoverinfo"><strong>',
                        'Number of upvotes in ' + geo.properties.name,
                        ': ' + data.numberOfWhatever,
                        '</strong></div>'].join('');            
            }
          },
        done: function(datamap) {
            datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
              //triggered by clicking on a country
/*                    let link = "popup.html#"
                link = link + geography.properties.name
                window.open(link, "_blank");*/
                let fullCountry = geography.properties.name
                let iso = getIsoThree(fullCountry)
                let popup = document.getElementById("popup")
                let close = document.getElementById("close")
                popup.style.display="block"
                close.onclick = function(){
                  popup.style.display = "none"
                }
                window.onclick = function(event){
                  if (event.target == popup){
                    popup.style.display == "none"
                  }
                }
                let popupHead = document.getElementById("popupHead")
                let popupBody = document.getElementById("popupBody")
                let popupFoot = document.getElementById("popupFoot")
                popupHead.innerHTML = "You clicked on " + fullCountry
                popupBody.innerHTML = fullCountry + "'s 3 letter ISO is " + iso

            });
          }
        })
        map.legend({labels: {minValue: minValue, two: two, halfWay: halfWay,four: four, maxValue: maxValue}})

    window.addEventListener('resize', function() {
        map.resize();
    });
  }


