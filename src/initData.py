import mysql.connector
import json
from urllib.request import urlopen


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

def updateFile():
    url1 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json'
    url2 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json'
    url3 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json'

    with open('../data/fiches_installations.json', 'wb') as datafile1:
        datafile1.write(urlopen(url1).read())
        print('Ecriture fiches_installations.json finie')

    with open('../data/fiches_equipements.json', 'wb') as datafile2:
        datafile2.write(urlopen(url2).read())
        print('Ecriture fiche_equipements.json finie')

    with open('../data/fiches_activites.json', 'wb') as datafile3:
        datafile3.write(urlopen(url3).read())
        print('Ecriture fiches_activites.json finie')


#Accès aux fichiers de données
chemins={
    'activites' : '../data/fiches_activites.json',
    'equipements' : '../data/fiches_equipements.json',
    'install' : '../data/fiches_installations.json'
}


#On crée des jeux de données traitées
#updateFile()


dataInstall = parseFileInstall(json.load(open(chemins['install'])))
dataEquip = parseFileEquip(json.load(open(chemins['equipements'])))
dataAct = parseFileAct(json.load(open(chemins['activites'])))

#print(dataInstall)
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

insertions["install"] = ("INSERT IGNORE INTO `INSTALLATIONS` "\
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
insertions["equip"] = ("INSERT IGNORE INTO `EQUIPEMENTS` "\
               "VALUES (%s, %s, %s)")
insertions["act"] = ("INSERT IGNORE INTO `ACTIVITES` "\
               "VALUES (%s, %s, %s, %s)")

cursor.executemany(insertions["install"], dataInstall)
cursor.executemany(insertions["act"], dataAct)
cursor.executemany(insertions["equip"], dataEquip)



database.commit()

cursor.close()
database.close()
