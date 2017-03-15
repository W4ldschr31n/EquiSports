$(document).ready(function(){

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
      $.getJSON("rechercheBD?commune="+$("#texteCommune").val()
      +"&activite="+$("#texteActivite").val()
      +"&niveau="+$("#listeNiveaux").val(),
      function(data){
        for (var i in data){
          $("ul").append("<li><a=\"#\"><span class=\"souligner\">"+data[i].insNom+"</span><br />"+data[i].actNom+"<br />"+data[i].nomCommune+" </a></li>");

        }
      });
    });
});
