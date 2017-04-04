import json
#Bibliothèques du projet
import sys
path ="/hometu/etudiants/r/i/E155059S/PycharmProjects/ProdLog/src/controller"
sys.path.append(path)
from dao import *
from bottle import *

#Accueil du site
@route('/')
def index():
    return static_file("site.html", root='./vue/html')

#Ressources utilisées
@route('/img/<filename>')
def routeIMG(filename):
    return static_file(filename, root='./vue/img')

@route('/css/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/css')

@route('/script/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/script')

#Requêtes AJAX
@route("/listeCommunes")
def getListeCommunes():
    return json.dumps(listeCommunes())

@route("/listeActivites")
def getListeActivites():
    return json.dumps(listeActivites())

@route("/listeNiveaux")
def getListeNiveaux():
    return json.dumps(listeNiveaux())

@route('/rechercheBD', method='GET')
def resultat():
    commune = request.query.commune
    activite = request.query.activite
    niveau = request.query.niveau
    return json.dumps(find(commune,activite,niveau))

#Erreurs
@error(404)
def error404(error):
    return static_file("404.html", root='./vue/html')

@error(500)
def error500(error):
    return "On n'a pas prévu ce cas, désolé, vous avez cassé notre code..."

#Lancement
run(host='0.0.0.0', port=8666, debug=True)
