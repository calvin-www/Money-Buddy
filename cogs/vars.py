from collections import defaultdict
import json

expenses = defaultdict(dict)
with open("cogs/db.JSON", "r") as jsonFile:
    data = json.load(jsonFile)

for key,value in data.items():
    expenses[int(key)] = value



def update_db():
    jsonfile = open('cogs/db.JSON', mode = 'w+')
    json.dump(expenses, jsonfile)
    jsonfile.close()


