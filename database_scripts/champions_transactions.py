import requests, json
from collections import defaultdict
import pymongo
import cassiopeia as cass
from DBKEYS import user, passcode
from RIOTAPIKEY import key

RIOTAPIKEY = key

# Database info
DBUSER = user
DBPASS = passcode
mongoclient = pymongo.MongoClient("mongodb+srv://%s:%s@ndsu-csci479-5ri0h.mongodb.net/test?retryWrites=true&w=majority" % (DBUSER, DBPASS))
db = mongoclient.frequentoflegends
col = db.matches_championsonly
cursor = col

# Cassioepeia info
RIOTAPIKEY = key
cass.set_riot_api_key(RIOTAPIKEY)
cass.set_default_region("NA")

  
    return "key doesn't exist"


# No. of champions currently in game
number_of_champions = len(cass.get_champions())

# Transaction table of all champions by matches played. The format of the table is as follows:
#           Champ1 | Champ2 | Champ3| ...
#   Match1      1       0       0
#   Match2      0       1       1
#   Match3      1       1       1
# 
# The 1 represents a match where the champion was played and won

winning_champs_transaction_table = []

# This stores the equivalent ID's of champions put into the transaction table. While there are 140+ champions in the game, some have ID's stretching as far as the 300's. This sytem allows us to instead create our own ID's in place

transaction_table_ids_lookup = list()

# DATABASE RETRIEVALS
winning_champs = []
for document in cursor.find(): #Can use .limit(n) to reduce for testing
    winning_champs.append(document)

# TRANSACTION TABLE
for match in winning_champs:
    win_transaction = [0] * number_of_champions

    # Match[2] is the string names of the champions
    for champ in match.get('winning_champions'):
        if champ not in transaction_table_ids_lookup:

            transaction_table_ids_lookup.append(champ)

        champ_index = transaction_table_ids_lookup.index(champ)
        win_transaction[champ_index] = 1
        
    winning_champs_transaction_table.append(win_transaction)

test = open('win_transactions.txt', 'a')
print(transaction_table_ids_lookup, file=test)
for match in winning_champs_transaction_table:
    print(match, file=test)
test.close()

