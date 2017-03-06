import mysql.connector
from pprint import pprint
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
#On défini les paramètres de connection à la base
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



"""
#On crée une nouvelle table (ça marche)
creerTable = "CREATE TABLE `departments` (`dept_no` char(4) NOT NULL,"\
    "  `dept_name` varchar(40) NOT NULL,"\
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"\
    ") ENGINE=InnoDB"
cursor.execute(creerTable)
"""


"""
#Créer plusieurs tables (marche?)
TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")
for name in TABLES.keys():
    print(name)
    cursor.execute(TABLES[name])
"""

"""
#Insertion d'un tuple (ça marche)
insererTuple = "INSERT INTO `departments` VALUES(456,'test');"
cursor.execute(insererTuple)
"""

"""
#Insertion de plusieurs tuples (ça marche)
stmt = ("INSERT INTO `departments` "\
               "VALUES (%s, %s)")
data = [
  (123,'finance'),
  (456, 'marketing'),
  (789, 'bowling'),
]
cursor.executemany(stmt, data)

"""

'''
#Récupération de données des résultats (ça marche)
query = ("SELECT insNom, nomCommune FROM INSTALLATIONS "
         "WHERE codePostal BETWEEN %s AND %s")
codeLow = 44130
codeHigh = 44150


cursor.execute(query, (codeLow, codeHigh))

for (insNom, nomCommune) in cursor:
    print("Nom installation : {} à {}".format(insNom,nomCommune))
'''


database.commit();

cursor.close()

#On se déconnecte
database.disconnect()
