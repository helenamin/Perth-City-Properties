

//create streetmap map layer
var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  });

//create satelite map layer
var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "satellite-streets-v9",
  accessToken: API_KEY
})

// Create myMap to set the whole layout for the map
var myMap = L.map("map", {
    center: [25, -30],
        zoom: 2.5,
        layers: [streetmap]
      });






    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {
        
    };
    
    legend.addTo(myMap);






    var baseMaps = {
        Street : streetmap,
        Satellite : satellite
    };

    var overlayMaps = {
 
      };
    
    // Adding layer to control the map
        L.control.layers(baseMaps, overlayMaps).addTo(myMap);


    });
});
