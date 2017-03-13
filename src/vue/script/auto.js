$(document).ready(function(){

    $.getJSON("listeCommunes", function(data){
      for (var i = 0; i < data.length; i++) {
        $("#listeCommunes").append("<option value='"+data[i]+"'>");
      }
    });

    $.getJSON("listeActivites", function(data){
      for (var i = 0; i < data.length; i++) {
        $("#listeActivites").append("<option value='"+data[i]+"'>");
      }
    });

    $.getJSON("listeNiveaux", function(data){
      for (var i = 0; i < data.length; i++) {
        $("#listeNiveaux").append("<option value='"+data[i]+"'>"+data[i]+"</option>");
      }
    });
});
