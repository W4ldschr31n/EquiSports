import mysql.connector
import json


#On définit des méthodes pour extraire les donnée intéressantes selon les fichiers (stockés sur le disque)

def parseFileInstall(data):
    dataInstall = data["data"]
    result = [ (tuple["InsNumeroInstall"],tuple["geo"]["name"],tuple["InsCodePostal"],tuple["ComLib"],tuple["InsNoVoie"],tuple["InsLibelleVoie"],tuple["Longitude"],tuple["Latitude"]) for tuple in dataInstall]
    return result

def parseFileEquip(data):
    dataEquip = data["data"]
    result = [(tuple["InsNumeroInstall"],tuple["EquipementId"],tuple["EquNom"]) for tuple in dataEquip]
    return result

def parseFileAct(data):
    dataAct = data["data"]
    result = [(tuple["EquipementId"],tuple["ActCode"],tuple["ActLib"],tuple["ActNivLib"]) for tuple in dataAct]
    return result

#Accès aux fichiers de données
chemins={
    'activites' : '../data/fiches_activites.json',
    'equipements' : '../data/fichesEquipements.json',
    'install' : '../data/fiches_installations.json'
}


#On crée des jeux de données traitées
dataInstall = parseFileInstall(json.load(open(chemins['install'])))
#dataEquip = parseFileAct(json.load(open(chemins['equipements'])))
#dataAct = parseFileAct(json.load(open(chemins['activites'])))

print(dataInstall)
#print(dataEquip)
#print(dataAct)

parameters ={
'host' : "infoweb",
'user' : "E155059S",
'database' : "E155059S",
'password': "E155059S"
}

#On se connecte à la base
database = mysql.connector.connect(**parameters)

#On vérifie qu'on est connecté
print("Connecté :" ,database.is_connected())

#On crée un curseur pour effectuer des opérations
cursor = database.cursor()

insertions={}

insertions["install"] = ("INSERT INTO `INSTALLATIONS` "\
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
insertions["equip"] = ("INSERT INTO `EQUIPEMENTS` "\
               "VALUES (%s, %s, %s)")
insertions["act"] = ("INSERT INTO `ACTIVITES` "\
               "VALUES (%s, %s, %s, %s)")

cursor.executemany(insertions["install"], dataInstall)
cursor.executemany(insertions["equip"], dataEquip)
cursor.executemany(insertions["act"], dataAct)


database.commit()

cursor.close()
database.close()
