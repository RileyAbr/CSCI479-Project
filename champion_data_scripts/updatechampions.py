import requests, json

import pymongo
import database_scripts.DBKEYS as DBKEYS

# MongoDB database info
DBUSER = DBKEYS.user
DBPASS = DBKEYS.passcode
mongoclient = pymongo.MongoClient("mongodb+srv://%s:%s@ndsu-csci479-5ri0h.mongodb.net/test?retryWrites=true&w=majority" % (DBUSER, DBPASS))
db = mongoclient.pythoninsert
col = db.championdata
cursor = col.find({}).sort("key", 1)

def json_print(json_str):
    text = json.dumps(json_str, sort_keys=True, indent=4)
    print(text)

count = 0

champ_key = 1

for document in cursor:
    champ_key_str = document["key"]
    champ_key_int = int(champ_key_str)

    col.update_one({
        "key": champ_key_str
    }, {
        "$set": {
        "num_key": champ_key_int}
    }, upsert=False)

    count += 1

for document in cursor:
    print(document["key"])
    print()

print(str(count) + " champions")