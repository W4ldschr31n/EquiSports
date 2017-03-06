from bottle import *
import mysql.connector
@route('/')
def index():
    return "Bienvenue sur notre application !"

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
