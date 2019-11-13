import requests, json, time
import pymongo
import cassiopeia as cass

RIOTAPIKEY = 'RGAPI-009f485d-0839-4b71-ab2b-17cc6df47565'

# Database info
DBUSER = "rileyabrahamson_ad"
DBPASS = "Lucian44"
mongoclient = pymongo.MongoClient("mongodb+srv://%s:%s@ndsu-csci479-5ri0h.mongodb.net/test?retryWrites=true&w=majority" % (DBUSER, DBPASS))
db = mongoclient.frequentoflegends
col = db.matches_championsonly

# Cassioepeia info
cass.set_riot_api_key(RIOTAPIKEY)
cass.set_default_region("NA")

# FUNCTIONS
def get_winning_champions(team):
    champion_names = []
    champion_keys = []
    for player in team.participants:
        champion_names.append(player.champion.name)
        champion_keys.append(player.champion.id)
    return [champion_names, champion_keys]


# This is a completely arbitrary starting value I obtained by putting in the username of a friend
match_id = 3204722627

# Loop counter that only increments when a match exists
successful_matches = 0
# DATABASE INSERTIONS
while successful_matches < 1000:
    winning_champions = []
    match = cass.get_match(match_id)
    
    # Check if match_id is valid
    if match.exists and match.mode.value == "CLASSIC" and match.map.id == 11:
        # For Blue Team wins
        if match.blue_team.win:
            winning_champions = get_winning_champions(match.blue_team)
        #For Red Team wins
        else:
            winning_champions = get_winning_champions(match.red_team)

        winning_match = {
            'match_id': match_id,
            "winning_champions": winning_champions[0],
            'winning_champions_keys': winning_champions[1]
        }

        # Insert champion list into the database
        col.insert_one(winning_match)

        # Increment counter
        successful_matches += 1
        print("Match added!")
    
    match_id += 1
    time.sleep(0.5)