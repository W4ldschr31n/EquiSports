import mysql.connector

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

#Création des tables

TABLES = {}
TABLES['INSTALLATIONS'] = (
    "CREATE TABLE `INSTALLATIONS` ("
    "  `idIns` INT(11) NOT NULL,"
    "  `insNom` VARCHAR(40) NOT NULL,"
    "  `codePostal` VARCHAR(5) NOT NULL,"
    "  `nomCommune` VARCHAR(40) NOT NULL,"
    "  `numRue` INT(10) NOT NULL,"
    "  `nomRue` VARCHAR(40) NOT NULL,"
    "  `longitude` FLOAT NOT NULL,"
    "  `latitude` FLOAT NOT NULL,"
    "  PRIMARY KEY (`idIns`)"
    ") ENGINE=InnoDB")

TABLES['EQUIPEMENTS'] = (
    "CREATE TABLE `EQUIPEMENTS` ("
    "  `idIns` INT(11) NOT NULL,"
    "  `idEqu` INT(11) NOT NULL,"
    "  PRIMARY KEY (`idIns`,`idEqu`),"
    "  FOREIGN KEY(`idIns`) REFERENCES `INSTALLATIONS`(`idIns`),"
    "  FOREIGN KEY(`idEqu`) REFERENCES `EQUIPEMENTS`(`idEqu`)"
    ") ENGINE=InnoDB")
TABLES['ACTIVITES'] = (
    "CREATE TABLE `ACTIVITES` ("
    "  `idEqu` INT(11) NOT NULL,"
    "  `actCode` INT(11) NOT NULL,"
    "  `actNom` VARCHAR(40),"
    "  `actNiveau` VARCHAR(20)"
    ") ENGINE=InnoDB")

for name in TABLES.keys():
    print(name)
    cursor.execute(TABLES[name])


database.commit()
