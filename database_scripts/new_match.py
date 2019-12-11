import requests
import json
import time
import pymongo
import cassiopeia as cass
from DBKEYS import user, passcode
from RIOTAPIKEY import key

# Database info
DBUSER = user
DBPASS = passcode
mongoclient = pymongo.MongoClient(
    "mongodb+srv://%s:%s@ndsu-csci479-5ri0h.mongodb.net/test?retryWrites=true&w=majority" % (DBUSER, DBPASS))
db = mongoclient.frequentoflegends
win_champs_col = db.winning_champs
loss_champs_col = db.losing_champs

# Cassioepeia info
RIOTAPIKEY = key
cass.set_riot_api_key(RIOTAPIKEY)
cass.set_default_region("NA")


# FUNCTIONS
def get_champions(team):
    champion_names = []
    champion_keys = []
    for player in team.participants:
        champion_names.append(player.champion.name)
        champion_keys.append(player.champion.id)
    return [champion_names, champion_keys]


print(time.time())
sum = cass.get_summoner(name="DBoy9")

new_match = cass.get_match_history(sum)

print(new_match)
