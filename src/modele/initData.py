import mysql.connector
import json
import csv
from urllib.request import urlopen


#On définit des méthodes pour extraire les donnée intéressantes selon les fichiers (stockés sur le disque)

def parseFileInstall():
    result = []
    with open(chemins["installations"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        for row in reader:
            result.append([row["Numéro de l'installation"],row["Nom usuel de l'installation"],row["Code postal"],row["Nom de la commune"],row["Numero de la voie"],row["Nom de la voie"]])
            i=i+1
        print(i)
    return result

def parseFileEquip():
    result = []
    with open(chemins["equipements"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        for row in reader:
            result.append([row["InsNumeroInstall"],row["EquipementId"],row["EquNom"],row["EquGpsX"],row["EquGpsY"]])
            i=i+1
        print(i)
    return result

def parseFileAct():
    result = []
    with open(chemins["activites"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        for row in reader:
            result.append([row["EquipementId"],row["ActCode"],row["ActLib"],row["ActNivLib"]])
            i=i+1
        print(i)
    return result

def updateFile():
    url1 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv'
    url2 = 'http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv'
    url3 = 'http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv'

    with open('../data/fiches_installations.csv', 'wb') as datafile1:
        datafile1.write(urlopen(url1).read())
        print('Ecriture fiches_installations.csv finie')

    with open('../data/fiches_equipements.csv', 'wb') as datafile2:
        datafile2.write(urlopen(url2).read())
        print('Ecriture fiche_equipements.csv finie')

    with open('../data/fiches_activites.csv', 'wb') as datafile3:
        datafile3.write(urlopen(url3).read())
        print('Ecriture fiches_activites.csv finie')


#Accès aux fichiers de données
chemins={
    'activites' : '../data/fiches_activites.csv',
    'equipements' : '../data/fiches_equipements.csv',
    'installations' : '../data/fiches_installations.csv'
}


#On crée des jeux de données traitées
#updateFile()




dataInstall = parseFileInstall()
dataEquip = parseFileEquip()
dataAct = parseFileAct()

print(dataInstall)
print(dataEquip)
print(dataAct)

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
               "VALUES (%s, %s, %s, %s, %s, %s)")
insertions["act"] = ("INSERT IGNORE INTO `ACTIVITES` "\
               "VALUES (%s, %s, %s, %s)")
insertions["equip"] = ("INSERT INTO `EQUIPEMENTS` "\
               "VALUES (%s, %s, %s, %s, %s)")


cursor.executemany(insertions["install"], dataInstall)
cursor.executemany(insertions["act"], dataAct)
cursor.executemany(insertions["equip"], dataEquip)

database.commit()

cursor.close()
database.close()
