#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
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

'''
#On récupère des résultats (ça marche)
query = ("SELECT insNom, nomCommune FROM INSTALLATIONS "
         "WHERE codePostal BETWEEN %s AND %s")
codeLow = 44130
codeHigh = 44150


cursor.execute(query, (codeLow, codeHigh))

for (insNom, nomCommune) in cursor:
    print("Nom installation : {} à {}".format(insNom,nomCommune))
'''
cursor.close()

database.close()
