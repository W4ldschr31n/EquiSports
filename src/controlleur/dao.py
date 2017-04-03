import mysql.connector

#Données pour se connecter à la BDD
parameters ={
        'host' : "infoweb",
        'user' : "E155059S",
        'database' : "E155059S",
        'password': "E155059S"
        }

def listeCommunes():
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()

    query = "SELECT nomCommune from INSTALLATIONS group by nomCommune"

    cursor.execute(query)

    listeResultat=[]
    for (resultat) in cursor:
       listeResultat.append(resultat[0])

    cursor.close()
    database.close()

    return listeResultat

def listeActivites():
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()
    #On évite les activites non declarees
    query = "SELECT actNom from ACTIVITES where actCode>0 group by actNom"

    cursor.execute(query)

    listeResultat=[]
    for (resultat) in cursor:
       listeResultat.append(resultat[0])

    cursor.close()
    database.close()

    return listeResultat

def listeNiveaux():
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()
    #On évite les niveaux non-définis
    query = "SELECT actNiveau from ACTIVITES actNiveau where actNiveau is not null group by actNiveau"

    cursor.execute(query)

    listeResultat=[]
    for (resultat) in cursor:
       listeResultat.append(resultat[0])

    cursor.close()
    database.close()

    return listeResultat

#Cette méthode est un "template" de requête, elle sélectionne automatiquement les données spécifiées ci-dessous avec une contrainte passée en paramètre
def requeteCondition(condition):

    champsInteressants = "a.actNom, a.actNiveau, e.equNom, i.insNom, i.codePostal, i.nomCommune, i.nomRue, i.numRue, e.longitude, e.latitude"
    tables = "ACTIVITES a, EQUIPEMENTS e, INSTALLATIONS i"
    jointure = "a.idEqu=e.idEqu and e.idIns=i.idIns"

    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()


    query = ("SELECT "+champsInteressants+" from "+tables+" where "+jointure+" "\
             "and "+condition)

    cursor.execute(query)
    listeResultat=[]
    champs = ["actNom","actNiveau","equNom","insNom","codePostal","nomCommune","nomRue","numRue","longitude","latitude"]
    for (resultat) in cursor:
        #On crée une liste de dictionnaires pour retrouver facilement les champs une fois que l'on parse en JSON
       listeResultat.append({champs[i] : resultat[i] for i in range(0,len(resultat))})
    cursor.close()

    database.close()

    return listeResultat

def findByCom(commune, activite, niveau):

    return requeteCondition("i.nomCommune = '"+commune+"'")

def findByAct(commune, activite, niveau):

    return requeteCondition("a.actNom = '"+activite+"'")


def findByNiv(commune, activite, niveau):

    return requeteCondition("a.actNiveau = '"+niveau+"'")

def findByComAct(commune, activite, niveau):

    return requeteCondition("i.nomCommune = '"+commune+"' and a.actNom = '"+activite+"'")

def findByActNiv(commune, activite, niveau):

    return requeteCondition("a.actNom = '"+activite+"' and a.actNiveau = '"+niveau+"'")

def findByComNiv(commune, activite, niveau):

    return requeteCondition("i.nomCommune = '"+commune+"' and a.actNiveau = '"+niveau+"'")

def findByNone(commune=None, activite=None, niveau=None):
    #Renvoie toute la base de données (lent)
    return requeteCondition("1")

def findByAll(commune, activite, niveau):

    return requeteCondition("i.nomCommune = '"+commune+"' and a.actNom = '"+activite+"' and a.actNiveau = '"+niveau+"'")


#Tableau de fonctions dont l'index correspond à la combinaison de paramètres utilisés selon un calcul binaire.
#commune correspond à 2^2, activite correspond à 2^1, et niveau correspond à 2^0
#chaque "bit" correspondant à un paramètre est levé si on utilise le paramètre.
#Par exemple si on veut utiliser la commune et l'activité, on utilise l'index "110" : 1*2^2+1*2^1+0*2^0 = 4+2+0 = 6
tabFonctions = [findByNone,findByNiv,findByAct,findByActNiv,findByCom,findByComNiv,findByComAct,findByAll]

def find(commune, activite, niveau):
    index = 0 if commune=="Tout" or commune=="" else 4
    index += 0 if activite=="Tout" or activite=="" else 2
    index += 0 if niveau=="Tout" or niveau=="" else 1
    return tabFonctions[index](commune, activite, niveau)
