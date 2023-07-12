function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: 28.7041,
            lng: 77.1025,
        },
        zoom: 8,
    });

    var marker = new google.maps.Marker({
        map: map,
        draggable: true,
    });

    google.maps.event.addListener(map, "click", function (event) {
        marker.setPosition(event.latLng);
        document.getElementById("id_latitude").value = event.latLng.lat();
        document.getElementById("id_longitude").value = event.latLng.lng();
    });
}
