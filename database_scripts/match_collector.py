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


# This is a completely arbitrary starting value
match_id = 3213024336

# Loop counter that only increments when a match exists
successful_matches = 0
# DATABASE INSERTIONS
while successful_matches < 1000:
    winning_champions = []
    losing_champions = []
    match = cass.get_match(match_id)

    # Check if match_id is valid
    # filter out bot matches
    if match.exists and match.mode.value == "CLASSIC" and match.map.id == 11 and (match.queue.id in (400, 420, 430, 440)):
        # Collect teams
        blue_team = get_champions(match.blue_team)
        red_team = get_champions(match.red_team)

        # For Blue Team wins
        if match.blue_team.win:
            winning_champions = blue_team
            losing_champions = red_team
        # For Red Team wins
        else:
            winning_champions = red_team
            losing_champions = blue_team

        winning_team = {
            'match_id': match_id,
            "winning_champions": winning_champions[0],
            'winning_champions_keys': winning_champions[1]
        }
        losing_team = {
            'match_id': match_id,
            "losing_champions": losing_champions[0],
            'losing_champions_keys': losing_champions[1]
        }

        # Insert winning and losing lists into the databases
        win_champs_col.insert_one(winning_team)
        loss_champs_col.insert_one(losing_team)

        # Increment counter
        successful_matches += 1
        print("Match added!")

        matchfile = open("correct_matches.txt", "a")
        print(match_id, file=matchfile)
        matchfile.close()

        if(successful_matches % 200 == 0):
            print("Pausing to avoid rate limit...")
            time.sleep(126)

    match_id += 1
    time.sleep(1)
