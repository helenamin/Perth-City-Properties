
// var location = [-31.9523 , 115.8613 ]

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

 
      
var suburbs = [{
  location: [-31.9523 , 115.8613],
  name: "Perth",
  population: "8,550,405"
},
{
  location: [-31.9463 , 115.8448],
  name: "West Perth",
  population: "8,550,405"
},
{
  location: [-31.9608 , 115.8746],
  name: "East Perth",
  population: "8,550,405"
},
{
  location: [-31.9470 , 115.8574],
  name: "Northbridge",
  population: "8,550,405"
},
{
  location: [-31.9814 , 115.8205],
  name: "Crawley",
  population: "8,550,405"
},
{
  location: [-31.9810 , 115.8039],
  name: "Nedlands",
  population: "8,550,405"
}]
      

// Loop through the suburbs array and create one marker for each suburb, bind a popup containing its name and ... add it to the map
for (var i = 0; i < suburbs.length; i++) {
  var sub = suburbs[i];
  L.marker(sub.location)
    .bindPopup("<h1>" + sub.name + "</h1> <hr> <h3>Population " + sub.population + "</h3>")
    .addTo(myMap);
}

// var marker = L.marker([-31.9523 , 115.8613 ], {
//   draggable: false,
//   title: "Suburb: Perth WA 6000"
//   }).addTo(myMap);


    //var legend = L.control({position: 'bottomright'});

    //legend.onAdd = function (map) {};
    
    //legend.addTo(myMap);



    // Adding layer to control the map

myMap();

		
		
		

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
    }).then(data=>{
      console.log(data.result)
      
      // if (suburb == "perth") {
      //   location = [-31.9523 , 115.8613];
      // } else if (suburb == "west_perth") {
      //   location = [-31.9463 , 115.8448];
      // } else if (suburb == "east_perth") {
      //   location = [-31.9608 , 115.8746];
      // } else if (suburb == "northbridge") {
      //   location = [-31.9470 , 115.8574];
      // } else if (suburb == "crawley") {
      //   location = [-31.9814 , 115.8205];
      // } else if (suburb == "nedlands") {
      //   location = [-31.9810 , 115.8039];
      // }
    
    })
    //
})
