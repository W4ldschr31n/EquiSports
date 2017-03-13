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

@route('/rechercheBD', method='POST')
def resultat():
    commune = request.forms.get("commune")
    activite = request.forms.get("activite")
    niveau = request.forms.get("niveau")
    return findByComActNiv(commune,activite,niveau)

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

@route('/autoCompleteActivite', method='POST')
def autoA(activite):
    parameters ={
    'host' : "infoweb",
    'user' : "E155059S",
    'database' : "E155059S",
    'password': "E155059S"
    }

    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()

    activite = request.forms.get("activite")
    query = ("SELECT a.actNom from ACTIVITES WHERE (a.actNom LIKE '"+activite+"' OR '"+activite+"' LIKE a.actNom) group by a.actNom")

    cursor.execute(query)
    s=""
    for (resultat) in cursor:
       s+= (str(resultat))+"<br>"
    cursor.close()

    database.close()

    return s;






@route('/installations/<champ>')
def getInstallationsChamp(champ = "*"):
    parameters ={
    'host' : "infoweb",
    'user' : "E155059S",
    'database' : "E155059S",
    'password': "E155059S"
    }

    #On se connecte à la base
    database = mysql.connector.connect(**parameters)

    #On crée un curseur pour effectuer des opérations
    cursor = database.cursor()


    #On récupère des résultats (ça marche)
    query = ("SELECT %s FROM INSTALLATIONS")

    cursor.execute(query, champ)

    for (resultat) in cursor:
        yield (resultat)
    cursor.close()

    database.close()


@route('/nomsAct')
def getnomsAct():
    parameters ={
    'host' : "infoweb",
    'user' : "E155059S",
    'database' : "E155059S",
    'password': "E155059S"
    }

    #On se connecte à la base
    database = mysql.connector.connect(**parameters)

    #On crée un curseur pour effectuer des opérations
    cursor = database.cursor()


    #On récupère des résultats (ça marche)
    query = ("SELECT `actNiveau` FROM ACTIVITES group by actNiveau")

    cursor.execute(query)
    s = ""
    for (resultat) in cursor:
        s+=str(resultat)+"<br />"
    cursor.close()

    database.close()
    return s
"""

run(host='localhost', port=8666, debug=True)
