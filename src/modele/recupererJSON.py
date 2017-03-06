import json
from pprint import pprint


with open("../data/localisationEquipements.json") as data_file:
    data1 = json.load(data_file)
'''
with open("../data/activitesFichesEquipements.json") as data_file:
    data2 = json.load(data_file)

with open("../data/fichesEquipements.json") as data_file:
    data3 = json.load(data_file)
'''
print({data1['data'][i]['COMMUNE'] for i in range(data1['nb_results'])})

commune = input("Nom de la commune\n")

print({data1['data'][i]['geo']['name'] for i in range(data1['nb_results']) if data1['data'][i]['COMMUNE']==commune})


#print({d['geo'] for d in data1['data']})
