import mysql.connector

champsInteressants = "a.actNom, a.actNiveau, e.equNom, i.insNom, i.codePostal, i.nomCommune, i.nomRue, i.numRue, i.longitude, i.latitude"
tables = "ACTIVITES a, EQUIPEMENTS e, INSTALLATIONS i"
jointure = "a.idEqu=e.idEqu and e.idIns=i.idIns"
parameters ={
        'host' : "infoweb",
        'user' : "E155059S",
        'database' : "E155059S",
        'password': "E155059S"
        }

def requeteCondition(condition):
    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()


    query = ("SELECT "+champsInteressants+" from "+tables+" where "+jointure+" "\
             "and "+condition)

    cursor.execute(query)
    s=""
    for (resultat) in cursor:
       s+= (str(resultat))+"<br>"
    cursor.close()

    database.close()

    return s

def findByCom(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' group by a.actNom")

def findByAct(commune, activite, niveau):

    return requeteCondition("a.actNom LIKE '%"+activite+"%' group by i.nomCommune")


def findByNiv(commune, activite, niveau):

    return requeteCondition("a.actNiveau = "+niveau+" group by i.insNom")

def findByComAct(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNom LIKE '%"+activite+"%' group by i.nomCommune")

def findByActNiv(commune, activite, niveau):

    return requeteCondition("a.actNom LIKE '%"+activite+"%' and a.actNiveau = "+niveau+" group by i.insNom")

def findByComNiv(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNiveau = "+niveau+" group by i.insNom")

def findByNone():

    return requeteCondition("1")

def findByAll(commune, activite, niveau):

    return requeteCondition("i.nomCommune LIKE '%"+commune+"%' and a.actNom LIKE '%"+activite+"%' and a.actNiveau = "+niveau)


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

