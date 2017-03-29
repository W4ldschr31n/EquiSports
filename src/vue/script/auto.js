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
        if(data.length==0){
            $("ul").append("<h1>Aucun résultat</h1>")
        }
        for (var i in data){
          $("ul").append("<li><a=\"#\"><span class=\"souligner\">"+data[i].insNom+"</span><br />"+data[i].actNom+"<br />"+data[i].nomCommune+" </a></li>");
          var description = "<h3>"+data[i].actNom+"</h3>"+data[i].actNiveau+"<br />"+data[i].insNom+"<br />"+(data[i].equNom==data[i].insNom?"":data[i].equNom+"<br />")+(data[i].numRue==0?"":data[i].numRue)+" "+(data[i].nomRue==""?"":data[i].nomRue+", ")+data[i].codePostal+", "+data[i].nomCommune;
      var infowindow = new google.maps.InfoWindow({
        content: description
      });
          addMarker(new google.maps.LatLng(data[i].latitude,data[i].longitude),infowindow,i*1000/data.length);
        }
        setMapOnAll(map);
        $("#spinner").attr("max",data.length);
        $("#spinner").val(data.length);
      });

    });

    $("#advCircle").on("click",function(){
        dragCircleOnNextClick = true;
    });

   google.maps.event.addListener(map,"click", function (event) {
       if(dragCircleOnNextClick){
           for (var i =0;i<circle.length;i++){
               circle[i].setMap(null);
            }

            circle=[];
            circle.push(new google.maps.Circle({map: map,
                radius: 10000,
                center: event.latLng,
                fillColor: '#00F',
                fillOpacity: 0.1,
                strokeColor: '#000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                draggable: false,
                editable: true
            }));
            dragCircleOnNextClick = false;
        }
    } );



    $("#advOptions").on("change", function(){
        var enabled = $("#advOptions").prop("checked")
        if(enabled){
            $("#advCircle").prop("disabled",false);
            $("#spinner").prop("disabled",false);
            $("#advBoutonDisabled").attr("id","advBouton");

        }
        else{
            $("#advCircle").prop("disabled",true);
            $("#spinner").prop("disabled",true);
            $("#advBouton").attr("id","advBoutonDisabled");
        }

    });


    $("#spinner").change(function(){
        for (var i =0; i < $("#spinner").val(); i++) {
            console.log(i);
            markers[i].setMap(map);
        }
        for (var i = $("#spinner").val(); i < markers.length; i++) {
            console.log(i);
            markers[i].setMap(null);
        }
    });

});
        // Adds a marker to the map and push to the array.
        function addMarker(location,infowindow,timeout) {
        window.setTimeout(function(){
            var marker = new google.maps.Marker({
                position: location,
                map: map
              });
               marker.addListener('click', function() {
               if(openWindow){
                    openWindow.close()
               }
               openWindow = infowindow;
               infowindow.open(map, marker);
               });

              markers.push(marker);
            },timeout);

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
