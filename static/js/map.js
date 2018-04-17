//example data copied from server
function map(){
    let series = [
        ["BLR",75],["BLZ",43],["RUS",50],["RWA",88],["SRB",21],["TLS",43],
        ["REU",21],["TKM",19],["TJK",60],["ROU",4],["TKL",44],["GNB",38],
        ["GUM",67],["GTM",2],["SGS",95],["GRC",60],["GNQ",57],["GLP",53],
        ["JPN",59],["GUY",24],["GGY",4],["GUF",21],["GEO",42],["GRD",65],
        ["GBR",14],["GAB",47],["SLV",15],["GIN",19],["GMB",63],["GRL",56],
        ["ERI",57],["MNE",93],["MDA",39],["MDG",71],["MAF",16],["MAR",8],
        ["MCO",25],["UZB",81],["MMR",21],["MLI",95],["MAC",33],["MNG",93],
        ["MHL",15],["MKD",52],["MUS",19],["MLT",69],["MWI",37],["MDV",44],
        ["MTQ",13],["MNP",21],["MSR",89],["MRT",20],["IMN",72],["UGA",59],
        ["TZA",62],["MYS",75],["MEX",80],["ISR",77],["FRA",54],["IOT",56],
        ["SHN",91],["FIN",51],["FJI",22],["FLK",4],["FSM",69],["FRO",70],
        ["NIC",66],["NLD",53],["NOR",7],["NAM",63],["VUT",15],["NCL",66],
        ["NER",34],["NFK",33],["NGA",45],["NZL",96],["NPL",21],["NRU",13],
        ["NIU",6],["COK",19],["XKX",32],["CIV",27],["CHE",65],["COL",64],
        ["CHN",16],["CMR",70],["CHL",15],["CCK",85],["CAN",76],["COG",20],
        ["CAF",93],["COD",36],["CZE",77],["CYP",65],["CXR",14],["CRI",31],
        ["CUW",67],["CPV",63],["CUB",40],["SWZ",58],["SYR",96],["SXM",31]];

        //expected arrangment: {"countryName": {"fillColor": #colorcode, "numberOfWhatever": num}}
        let dataSet = {}

/*        for(let item in rawDataSet){
          dataSet[getIsoThree(item)] = rawDataSet[item]
        }*/

        let values = []

        //fetching values to determine min/max
        for (let item of series){
          values.push(item[1])
        }

        var minValue = Math.min(...values)
        var maxValue = Math.max(...values)

        //using d3 scale module to build a scale between dark green (light) and dark red (heavy)
        var colorScale = d3.scale.linear()
          .domain([minValue, maxValue])
          .range(["#FFFFB2","#BD0026"])

        var halfWay = Math.round(maxValue / minValue)
        var two = Math.round(halfWay / minValue)
        var four = Math.round((maxValue - minValue) * .75)

        //fetch country/value and popluate the dataSet
        var fills = {}
        for (let item of series){
          let country = item[0]
          let val = item[1]

          dataSet[country] = {"fillColor": colorScale(val), "numberOfWhatever": val}


        }
        //generate a map
        var map =  new Datamap({
          element: document.getElementById("map"),
          responisve : true,
          fills: {defaultFill: "white", minValue: "#FFFFB2", two: "#EFC08F", halfWay: "#DE806C", four: "#CE4049", maxValue: "BD0026"},
          data: dataSet,
          projection: "mercator",
          geographyConfig: {
            highlightFillColor: '#565656',
            borderColor: '#444',
            borderWidth: 0.5,
            popupTemplate: function(geo, data){
                return ['<div class="hoverinfo"><strong>',
                        'Number of articles in ' + geo.properties.name,
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


