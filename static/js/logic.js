

//create streetmap map layer
var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  });


// Create myMap to set the whole layout for the map
var myMap = L.map("map", {
    center: [-31.9523 , 115.8613 ], //centralise the map
        zoom: 12,
        layers: [streetmap]
      });




    //var legend = L.control({position: 'bottomright'});

    //legend.onAdd = function (map) {};
    
    //legend.addTo(myMap);



    // Adding layer to control the map
	myMap.invalidateSize();

		
		
		
		

//for inputs limit
 function onlyNumberKey(evt) {
          
        // Only ASCII character in that range allowed
        var ASCIICode = (evt.which) ? evt.which : evt.keyCode
        if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
            return false;
        return true;
    }
		
function errorcatch() {
  var bedroom = document.getElementById("bedroom_range").value;
  var bathroom = document.getElementById("bathroom_range").value;
  var carspace = document.getElementById("carspaces_range").value;
  var landsize = document.getElementById("land").value;
  var builtsize = document.getElementById("built").value;
  var builtyear= document.getElementById("builtdate").value;
  var suburb = document.getElementById("suburbs").value;

  console.log(bedroom, bathroom, carspace,landsize,builtsize,builtyear,suburb)

}
