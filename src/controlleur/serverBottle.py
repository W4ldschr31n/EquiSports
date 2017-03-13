from bottle import *
import sys
path ="/hometu/etudiants/r/i/E155059S/PycharmProjects/ProdLog/src/controller"
sys.path.append(path)
from dao import *


# Variable "statiques" dont on a besoin pour l'autocomplétion



@route('/')
@route('/recherche')
def index():
    return static_file("index", root='./vue')

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

run(host='localhost', port=8666, debug=True)
