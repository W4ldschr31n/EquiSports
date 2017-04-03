import mysql.connector
import csv
from urllib.request import urlopen

#Ce programme permet de récupérer les données sur le site du conseil régional, puis de les insérer dans la base de données

#Accès aux fichiers de données
chemins={
    'activites' : '../data/fiches_activites.csv',
    'equipements' : '../data/fiches_equipements.csv',
    'installations' : '../data/fiches_installations.csv'
}



#On télécharge les fichiers sur le disque et on les enregistre sous un nom défini dans le répertoire data/
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


#On définit des méthodes pour extraire les données intéressantes selon les fichiers (stockés sur le disque)

def parseFileInstall():
    result = []
    with open(chemins["installations"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append([row["Numéro de l'installation"],row["Nom usuel de l'installation"],row["Code postal"],row["Nom de la commune"],row["Numero de la voie"],row["Nom de la voie"]])
    return result

def parseFileEquip():
    result = []
    with open(chemins["equipements"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append([row["InsNumeroInstall"],row["EquipementId"],row["EquNom"],row["EquGpsX"],row["EquGpsY"]])
    return result

def parseFileAct():
    result = []
    with open(chemins["activites"], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append([row["EquipementId"],row["ActCode"],row["ActLib"],row["ActNivLib"]])
    return result


#On crée des jeux de données traitées
updateFile()
dataInstall = parseFileInstall()
dataEquip = parseFileEquip()
dataAct = parseFileAct()

"""On peut les afficher si besoin
print(dataInstall)
print(dataEquip)
print(dataAct)
"""

#Paramètres de connexion à la BDD
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
#Les données du site pour les activites ne sont pas toujours bien écrites, on effectue un INSERT IGNORE pour ne pas arrêter l'exécution du programme
insertions["act"] = ("INSERT IGNORE INTO `ACTIVITES` "\
               "VALUES (%s, %s, %s, %s)")
insertions["equip"] = ("INSERT INTO `EQUIPEMENTS` "\
               "VALUES (%s, %s, %s, %s, %s)")

#On insère toutes nos données dans un ordre particulier pour les dépendances de la BDD
print("Insertion des installations...",end="")
cursor.executemany(insertions["install"], dataInstall)
print("faite")
print("Insertion des activites...",end="")
cursor.executemany(insertions["act"], dataAct)
print("faite")
print("Insertion des equipements...",end="")
cursor.executemany(insertions["equip"], dataEquip)
print("faite")
database.commit()

cursor.close()
database.close()
