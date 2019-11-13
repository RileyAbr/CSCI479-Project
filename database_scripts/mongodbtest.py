import pymongo

import database_scripts.DBKEYS as DBKEYS

# MongoDB database info
DBUSER = DBKEYS.user
DBPASS = DBKEYS.passcode
mongoclient = pymongo.MongoClient("mongodb+srv://%s:%s@ndsu-csci479-5ri0h.mongodb.net/test?retryWrites=true&w=majority" % (DBUSER, DBPASS))
db = mongoclient.pythoninsert
col = db.testinserts

testdict = { "name": "John", "address": "Highway 37" }

col.insert_one(testdict)