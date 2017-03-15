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
    print("lol")
    commune = request.query.get("commune")
    activite = request.query.get("activite")
    niveau = request.query.get("niveau")
    return json.dumps(findByComActNiv(commune,activite,niveau))

@route('/img/<filename>')
def routeIMG(filename):
    return static_file(filename, root='./vue/img')

@route('/css/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/css')

@route('/script/<filename>')
def routeCSS(filename):
    return static_file(filename, root='./vue/script')

@route('/autoCom', method="GET")
def autoCom():
    commune = request.query.get("comm")
    print(commune)
    return json.dumps(getCommunes(commune))

@route("/listeCommunes")
def getListeCommunes():
    return json.dumps(listeCommunes())

@route("/listeActivites")
def getListeActivites():
    return json.dumps(listeActivites())

@route("/listeNiveaux")
def getListeNiveaux():
    return json.dumps(listeNiveaux())

"""
@route('/doom')
def apocalypse():
    return findByNone();

@route('/rechercheC', method='POST')
def rechercheC():
    commune = request.forms.get("commune")
    return findByCom(commune);

@route('/rechercheA', method='POST')
def rechercheA():
    activite = request.forms.get("activite")
    return findByAct(activite);
"""

run(host='localhost', port=8666, debug=True)
