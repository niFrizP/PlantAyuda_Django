var map;
function initMap() {
 map = new google.maps.Map(document.getElementById('map'), {
   center: {lat: -36.8221543, lng: -73.0558035},
   zoom: 12,
 });
 var icon = {
  url: "https://cdn-icons-png.flaticon.com/512/2362/2362826.png", 
  scaledSize: new google.maps.Size(27, 32), 
  origin: new google.maps.Point(0,0), 
  anchor: new google.maps.Point(0, 0) 
};

 var marker = new google.maps.Marker({
   
   position: {lat: -36.7877238, lng: -73.1132868},
   map: map,
   icon: icon,
title: 'sucursal hualpen'
 });
 var marker = new google.maps.Marker({
    position: {lat: -36.838152, lng: -73.147673},
    map: map,
    icon: icon,
 title: 'sucursal san pedro'
  });
  

var marker = new google.maps.Marker({
    position: {lat: -36.822667, lng: -73.044247},
    map: map,
    icon: icon,
    title: 'sucursal de concepcion'
    
});
        

  
}