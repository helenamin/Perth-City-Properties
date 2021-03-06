

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
    center: [-31.955 , 115.853], //centralise the map
        zoom: 11,
        layers: [streetmap]
      });

var marker = L.marker([45.52, -122.67], {
  draggable: false,
  title: "Suburb: Perth WA 6000"
  }).addTo(myMap);


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
		
// function errorcatch() {
//   var bedroom = document.getElementById("bedroom_range").value;
//   var bathroom = document.getElementById("bathroom_range").value;
//   var carspace = document.getElementById("carspaces_range").value;
//   var landsize = document.getElementById("land").value;
//   var builtsize = document.getElementById("built").value;
//   var builtyear= document.getElementById("builtdate").value;
//   var suburb = document.getElementById("suburbs").value;

//   console.log(bedroom, bathroom, carspace,landsize,builtsize,builtyear,suburb)

// }

d3.select("#submit_this").on("click",()=>{
  console.log("Clicked!")
  var bedroom = document.getElementById("bedroom_range").value;
  var bathroom = document.getElementById("bathroom_range").value;
  var carspace = document.getElementById("carspaces_range").value;
  var landsize = document.getElementById("land").value;
  var builtsize = document.getElementById("built").value;
  var builtyear= document.getElementById("builtdate").value;
  var suburb = document.getElementById("suburbs").value;
  
  console.log(bedroom, bathroom, carspace,landsize,builtsize,builtyear,suburb)

  d3.json('/api/v1.0/predict', {
      method:"POST",
      body: JSON.stringify({
        Bedroom: bedroom,
        Bathroom: bathroom,
        Car_Spaces: carspace,
        Land_Size: landsize,
        Built_Size: builtsize,
        Built_Year: builtyear,
        Suburb: suburb
      }),headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    }).then(data=>{console.log(data.result)})
    //
})