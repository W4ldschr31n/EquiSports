import mysql.connector

#Paramètres pour se connecter à la base
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

#Nettoyage de la base dans un ordre particulier pour les dépendances des données
delete = ("EQUIPEMENTS", "ACTIVITES", "INSTALLATIONS")
for name in delete:
    try:
        print("Suppression de la table {}: ".format(name), end='')
        cursor.execute("DROP TABLE "+name)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("OK")
    

#Création des tables

TABLES = {}
TABLES['INSTALLATIONS'] = (
    "CREATE TABLE `INSTALLATIONS` ("
    "  `idIns` INT(11) NOT NULL,"
    "  `insNom` VARCHAR(100) NOT NULL,"
    "  `codePostal` VARCHAR(5) NOT NULL,"
    "  `nomCommune` VARCHAR(100) NOT NULL,"
    "  `numRue` INT(10) NOT NULL,"
    "  `nomRue` VARCHAR(100) NOT NULL,"
    "  PRIMARY KEY (`idIns`)"
    ") ENGINE=InnoDB")

TABLES['EQUIPEMENTS'] = (
    "CREATE TABLE `EQUIPEMENTS` ("
    "  `idIns` INT(11) NOT NULL,"
    "  `idEqu` INT(11) NOT NULL,"
    "  `equNom` VARCHAR(100) NOT NULL,"
    "  `longitude` FLOAT NOT NULL,"
    "  `latitude` FLOAT NOT NULL,"
    "  PRIMARY KEY (`idIns`,`idEqu`)"
    ") ENGINE=InnoDB")
TABLES['ACTIVITES'] = (
    "CREATE TABLE `ACTIVITES` ("
    "  `idEqu` INT(11) NOT NULL,"
    "  `actCode` INT(11) NOT NULL,"
    "  `actNom` VARCHAR(100),"
    "  `actNiveau` VARCHAR(100),"
    "  PRIMARY KEY (`idEqu`,`actCode`, `actNom`)"
    ") ENGINE=InnoDB")

#Creation des tables dans un ordre précis pour les dépendances des données
NAMES= ('INSTALLATIONS', 'EQUIPEMENTS', 'ACTIVITES')
for name in NAMES:
    try:
        print("Creation de la table {}: ".format(name), end='')
        cursor.execute(TABLES[name])
    except mysql.connector.Error as err:
            print(err.msg)
    else:
        print("OK")



database.commit()
cursor.close()
database.close()
