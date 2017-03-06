from urllib import urlopen

def parseFileInstall(data):
    dataInstall = data["data"]
    result = [ [tuple["InsNumeroInstall"],tuple["geo"]["name"],tuple["InsCodePostal"],tuple["ComLib"],tuple["InsNoVoie"],tuple["InsLibelleVoie"],tuple["Longitude"],tuple["Latitude"]] for tuple in dataInstall]
    return result

def parseFileEquip(data):
    dataEquip = data["data"]
    result = [[tuple["InsNumeroInstall"],tuple["EquipementId"],tuple["EquNom"]] for tuple in dataEquip]
    return result

def parseFileAct(data):
    dataAct = data["data"]
    result = [[tuple["EquipementId"],tuple["ActCode"],tuple["ActLib"],tuple["ActNivLib"]] for tuple in dataAct]
    return result

def updateFile():
    url1 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json'
    url2 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json'
    url3 = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json'

    with open('../data/fiches_installations.json', 'wb') as datafile1:
        datafile1.write(urlopen(url1).read())
        print('Ecriture fiches_installations.json finie')

    with open('../data/fichesEquipements.json', 'wb') as datafile2:
        datafile2.write(urlopen(url2).read())
        print('Ecriture ficheEquipements.json finie')

    with open('../data/fiches_activites.json', 'wb') as datafile3:
        datafile3.write(urlopen(url3).read())
        print('Ecriture fiches_activites.json finie')
