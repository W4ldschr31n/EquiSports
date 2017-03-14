import mysql.connector


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

    s=[]
    for (resultat) in cursor:
       s.append(resultat[0])

    cursor.close()
    database.close()

    return s

def listeActivites():
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()

    query = "SELECT actNom from ACTIVITES group by actNom"

    cursor.execute(query)

    s=[]
    for (resultat) in cursor:
       s.append(resultat[0])

    cursor.close()
    database.close()

    return s

def listeNiveaux():
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()

    query = "SELECT actNiveau from ACTIVITES group by actNiveau"

    cursor.execute(query)

    s=[]
    for (resultat) in cursor:
       s.append(resultat[0])

    cursor.close()
    database.close()

    return s

def getCommunes(commune):
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()
    print(commune)

    query = "SELECT nomCommune from INSTALLATIONS where nomCommune LIKE '%"+commune+"%' group by nomCommune"

    cursor.execute(query)

    s=[]
    for (resultat) in cursor:
       s.append(resultat[0])

    cursor.close()
    database.close()

    return s

#Cette méthode est un "template" de requête, elle sélectionne automatiquement les données spécifiées ci-dessous avec une contrainte passée en paramètre
def requeteCondition(condition):

    champsInteressants = "a.actNom, a.actNiveau, e.equNom, i.insNom, i.codePostal, i.nomCommune, i.nomRue, i.numRue, i.longitude, i.latitude"
    tables = "ACTIVITES a, EQUIPEMENTS e, INSTALLATIONS i"
    jointure = "a.idEqu=e.idEqu and e.idIns=i.idIns"

    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()


    query = ("SELECT "+champsInteressants+" from "+tables+" where "+jointure+" "\
             "and "+condition)

    cursor.execute(query)
    s=[]
    champs = ["actNom","actNiveau","equNom","insNom","codePostal","nomCommune","nomRue","numRue","longitude","latitude"]
    for (resultat) in cursor:
       s.append({champs[i] : resultat[i] for i in range(0,len(resultat))})
    cursor.close()

    database.close()

    return s

def findByCom(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' group by a.actNom")

def findByAct(commune, activite, niveau):

    return requeteCondition("a.actNom LIKE '%"+activite+"%' group by i.nomCommune")


def findByNiv(commune, activite, niveau):

    return requeteCondition("a.actNiveau LIKE '%"+niveau+"%' group by i.insNom")

def findByComAct(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNom LIKE '%"+activite+"%'")

def findByActNiv(commune, activite, niveau):

    return requeteCondition("a.actNom LIKE '%"+activite+"%' and a.actNiveau LIKE '%"+niveau+"%'")

def findByComNiv(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNiveau LIKE '%"+niveau+"%'")

def findByNone(commune, activite, niveau):

    return requeteCondition("1")

def findByAll(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNom LIKE '%"+activite+"%' and a.actNiveau LIKE '%"+niveau+"%'")


#Tableau de fonctions dont l'index correspond à la combinaison de paramètres utilisés selon un calcul binaire.
#niveau correspond à 2^0; activite correspond à 2^1 et commune correspond à 2^2
#chaque "bit" correspondant à un paramètre est levé si on utilise le paramètre.
#Par exemple si on veut utiliser la commune et l'activité, on utilise l'index 1*2^2+0*2^1+1*2^0 = 4+0+1 = 5
tabFonctions = [findByNone,findByNiv,findByAct,findByActNiv,findByCom,findByComNiv,findByComAct,findByAll]

def findByComActNiv(commune, activite, niveau):
    index = 0 if commune=="Tout" or commune=="" else 4
    index += 0 if activite=="Tout" or activite=="" else 2
    index += 0 if niveau=="Tout" or niveau=="" else 1
    return tabFonctions[index](commune, activite, niveau)
