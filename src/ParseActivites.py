
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
