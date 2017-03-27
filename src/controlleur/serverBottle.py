from bottle import *
import sys
import json
path ="/hometu/etudiants/r/i/E155059S/PycharmProjects/ProdLog/src/controller"
sys.path.append(path)
from dao import *


# Variable "statiques" dont on a besoin pour l'autocomplétion



@route('/')
@route('/recherche')
def index():
    return static_file("site.html", root='./vue/html')

@route('/rechercheBD', method='GET')
def resultat():
    commune = request.query.commune
    activite = request.query.activite
    niveau = request.query.niveau
    return json.dumps(find(commune,activite,niveau))

@route('/img/<filename>')
def routeIMG(filename):
    return static_file(filename, root='./vue/img')

@route('/css/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/css')

@route('/script/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/script')

@error(404)
def error404(error):
    return static_file("404.html", root='./vue/html')

@error(500)
def error500(error):
    return "On n'a pas prévu ce cas, désolé, vous avez cassé notre code..."

@route("/listeCommunes")
def getListeCommunes():
    return json.dumps(listeCommunes())

@route("/listeActivites")
def getListeActivites():
    return json.dumps(listeActivites())

@route("/listeNiveaux")
def getListeNiveaux():
    return json.dumps(listeNiveaux())


run(host='0.0.0.0', port=8666, debug=True)
