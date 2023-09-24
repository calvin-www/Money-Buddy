from collections import defaultdict
import json

#initialize the expenses map as a defaultdict so that new items can be easily added
expenses = defaultdict(dict)
#open json file as a permanent database
with open("cogs/db.JSON", "r") as jsonFile:
    data = json.load(jsonFile)

#write the json file into the expense map
for key,value in data.items():
    expenses[int(key)] = value


#updates the json map whenever called (preferably after every function that mutates expense)
def update_db():
    jsonfile = open('cogs/db.JSON', mode = 'w+')
    json.dump(expenses, jsonfile)
    jsonfile.close()


