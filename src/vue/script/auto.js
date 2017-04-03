$(document).ready(function(){
//On initialise la Google Maps
    initMap();
    //On se prépare à effectuer les requêtes AJAX
    $("#listeCommunes").empty();
//On remplit les propositions pour les communes
    $.getJSON("listeCommunes", function(data){
      for (var i in data) {
        $("#listeCommunes").append("<option value='"+data[i]+"'>");
      }
    });
//On remplit le spropositions pour les activites
    $.getJSON("listeActivites", function(data){
      for (var i in data) {
        $("#listeActivites").append("<option value='"+data[i]+"'>");
      }
    });
//On remplit les propositions pour les niveaux
    $.getJSON("listeNiveaux", function(data){
      for (var i in data) {
        $("#listeNiveaux").append("<option value='"+data[i]+"'>"+data[i]+"</option>");
      }
    });

    //On désactive la recherche avancée
    $("#advCircle").prop("disabled",true);
    $("#spinner").prop("disabled",true);
    $("#advBouton").attr("id","advBoutonDisabled");


//Listener du bouton de recherche
    $("#go").on("click",function(){
    //On détruit les résultats précédents
      $("ul").empty();
      clearMarkers();
      deleteMarkers();
      //On effectue une requête AJAX avec les champs remplis
      $.getJSON("rechercheBD?commune="+$("#textCom").val()
      +"&activite="+$("#textAct").val()
      +"&niveau="+$("#listeNiveaux").val(),
      function(data){
        if(data.length==0){
        //Si on n'a pas de résultat correspondant
            $("ul").append("<h1>Aucun résultat</h1>")
        }
        else{

            //Sinon, on ajoute un marqueur pour chaque activité ainsi qu'un élément dans la liste de résultats
            for (var i in data){
              $("ul").append($("<li><a=\"#\"><span class=\"souligner\">"+data[i].insNom+"</span><br />"+data[i].actNom+"<br />"+data[i].nomCommune+" </a></li>"));

              console.log("boucle : "+i);
              var description = "<h3>"+data[i].actNom+"</h3>"+data[i].actNiveau+"<br />"+data[i].insNom+"<br />"+(data[i].equNom==data[i].insNom?"":data[i].equNom+"<br />")+(data[i].numRue==0?"":data[i].numRue)+" "+(data[i].nomRue==""?"":data[i].nomRue+", ")+data[i].codePostal+", "+data[i].nomCommune;
              //Informations affichées lors du click sur un marqueur
             var infowindow = new google.maps.InfoWindow({
                 content: description
             });
              addMarker(new google.maps.LatLng(data[i].latitude,data[i].longitude),infowindow,i*1000/data.length);
            }
            //On ajoute un click listener sur chaque élément de la liste
            $("li").each(function(i){
            console.log("each : "+i);
            //Cela déclenche le click du marqueur associé
                $(this).on("click",function(){
                    google.maps.event.trigger(markers[i],"click");
                    }
                )});
            if($("#advOptions").prop("checked")){
                reviewMarkers();
            }
            else{
                setMapOnAll(map);
            }

        }

      });
    });

//Si on click sur le bouton approprié, le prochain click déplacera le cercle de restriction
    $("#advCircle").on("click",function(){
        dragCircleOnNextClick = true;
    });

//Si on click sur la map on déplace le cercle (à condition d'avoir clické avant sur le bouton)
   google.maps.event.addListener(map,"click", function (event) {
       if(dragCircleOnNextClick){
             console.log(event.latLng);
             circle.setCenter(event.latLng);
             dragCircleOnNextClick = false;
             reviewMarkers();
            }
    } );


//On peut activer ou désactiver la recherche dans le cercle
    $("#advOptions").on("change", function(){
        var enabled = $("#advOptions").prop("checked")
        if(enabled){
            $("#advCircle").prop("disabled",false);
            $("#spinner").prop("disabled",false);
            $("#advBoutonDisabled").attr("id","advBouton");
            showCircle();
            reviewMarkers();

        }
        else{
            $("#advCircle").prop("disabled",true);
            $("#spinner").prop("disabled",true);
            $("#advBouton").attr("id","advBoutonDisabled");
            hideCircle();
            showMarkers();
        }

    });

//Quand on touche au spinner cela change la taille du cercle, et met à jour les marqueurs
    $("#spinner").on("input",function(){
        circle.setRadius(parseFloat($("#spinner").val()));
        $("#rayon").text(Math.round($("#spinner").val()/(10*100))+"km");
        reviewMarkers();
    });

});
        // Crée un marqueur sur la GMaps et le stock dans un array
        function addMarker(location,infowindow) {
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
        }

        // Positionne le cercle sur une GMaps
        function setMapOfCircle(map){
            circle.setMap(map);
        }

        //Cache le cercle sans le supprimer
        function hideCircle(){
            setMapOfCircle(null);
        }

        //Réaffiche le cercle
        function showCircle(){
            setMapOfCircle(map);
        }

        //Affiche ou cache des marqueurs selon le rayon du cercle
        function reviewMarkers(){
        var latLngCircle = circle.getCenter();
        for (var i = 0; i < markers.length; i++) {
            var marker = markers[i];
            var latLngMarker = marker.getPosition();
            var dist = google.maps.geometry.spherical.computeDistanceBetween(latLngCircle, latLngMarker);
            if(dist<=circle.getRadius()){
                marker.setMap(map);
            }else{
                marker.setMap(null);
            }
          }
        }


        // Positionne tous les marqueurs stockés sur une GMaps
        function setMapOnAll(map) {
          for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
          }
        }

        // Enlève les marqueurs de la carte, mais les garde en mémoire
        function clearMarkers() {
          setMapOnAll(null);
        }

        // Afficher tous les marqueurs stockés sur la GMaps
        function showMarkers() {
          setMapOnAll(map);
        }

        // Supprime définitivement tous les marqueurs en mémoire
        function deleteMarkers() {
          clearMarkers();
          markers = [];
        }
