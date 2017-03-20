$(document).ready(function(){



initMap();
    $("#listeCommunes").empty();

    $.getJSON("listeCommunes", function(data){
      for (var i in data) {
        $("#listeCommunes").append("<option value='"+data[i]+"'>");
      }
    });

    $.getJSON("listeActivites", function(data){
      for (var i in data) {
        $("#listeActivites").append("<option value='"+data[i]+"'>");
      }
    });

    $.getJSON("listeNiveaux", function(data){
      for (var i in data) {
        $("#listeNiveaux").append("<option value='"+data[i]+"'>"+data[i]+"</option>");
      }
    });


    $("#go").on("click",function(){
      $("ul").empty();
      clearMarkers();
      deleteMarkers();
      $.getJSON("rechercheBD?commune="+$("#textCom").val()
      +"&activite="+$("#textAct").val()
      +"&niveau="+$("#listeNiveaux").val(),
      function(data){
        for (var i in data){
          $("ul").append("<li><a=\"#\"><span class=\"souligner\">"+data[i].insNom+"</span><br />"+data[i].actNom+"<br />"+data[i].nomCommune+" </a></li>");


          var description = "yo : "+data[i].actNom;

  var infowindow = new google.maps.InfoWindow({
    content: description
  });




          addMarker(new google.maps.LatLng(data[i].latitude,data[i].longitude),infowindow);
        }
        setMapOnAll(map);
      });
    });
});
        // Adds a marker to the map and push to the array.
        function addMarker(location,infowindow) {
          var marker = new google.maps.Marker({
            position: location,
            map: map
          });
           marker.addListener('click', function() {
           infowindow.open(map, marker);
           });

          markers.push(marker);
        }


        // Sets the map on all markers in the array.
        function setMapOnAll(map) {
          for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
          }
        }

        // Removes the markers from the map, but keeps them in the array.
        function clearMarkers() {
          setMapOnAll(null);
        }

        // Shows any markers currently in the array.
        function showMarkers() {
          setMapOnAll(map);
        }

        // Deletes all markers in the array by removing references to them.
        function deleteMarkers() {
          clearMarkers();
          markers = [];
        }
