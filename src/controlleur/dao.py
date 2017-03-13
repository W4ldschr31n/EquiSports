import mysql.connector
def yo(commune):
    parameters ={
        'host' : "infoweb",
        'user' : "E155059S",
        'database' : "E155059S",
        'password': "E155059S"
        }

    database = mysql.connector.connect(**parameters)
    cursor = database.cursor()


    query = ("SELECT a.actNom from ACTIVITES a, EQUIPEMENTS e, INSTALLATIONS i where a.idEqu=e.idEqu and e.idIns=i.idIns "\
             "and (i.nomCommune LIKE '"+commune+"' OR '"+commune+"' LIKE i.nomCommune) group by a.actNom")

    cursor.execute(query)
    s=""
    for (resultat) in cursor:
       s+= (str(resultat))+"<br>"
    cursor.close()

    database.close()

    return s
