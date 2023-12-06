// custom-map.js

// Create a map instance
var map = L.map('map').setView([0,0], 0);

// Add a custom tile layer (replace with your custom tile layer URL)
L.tileLayer('static/images/map{z}/{x}/{y}.png', {
    minZoom: 0, maxZoom: 1,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">Lebni Perez Maro</a>'
}).addTo(map);

// Add a marker
var marker = L.marker([51.5, -0.09]).addTo(map);

// Add a popup to the marker
marker.bindPopup('Test').openPopup();
