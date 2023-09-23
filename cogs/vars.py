from collections import defaultdict
import json

expenses = defaultdict(dict)
with open(r"C:\Users\calvi\OneDrive\Desktop\github\Money-Buddy\cogs\db.JSON", "r") as jsonFile:
    data = json.load(jsonFile)

for key,value in data.items():
    expenses[int(key)] = value



def update_db():
    jsonfile = open(r'C:\Users\calvi\OneDrive\Desktop\github\Money-Buddy\cogs\db.JSON', mode = 'w+')
    json.dump(expenses, jsonfile)
    jsonfile.close()


#expenses = {"groceries": [['12/12/12', 200, "Food"], ['12/2/12', 20, "Foaads"]],
 #           "subscriptions": [['12/25/12', 11.99, "spotify"], ['12/26/12', 15.99, "Netflix"]]}
#{user: {category:[sdgs]}}