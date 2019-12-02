import time, random
import cassiopeia as cass
from DBKEYS import user, passcode
from RIOTAPIKEY import key

# Cassioepeia info
RIOTAPIKEY = key
cass.set_riot_api_key(RIOTAPIKEY)
cass.set_default_region("NA")

summoner = cass.get_summoner(name="DBoy9")

# champions = cass.get_champions()

print(summoner)

history = cass.get_match_history(summoner)

base_id = 3197203518
blue_wins = 0
red_wins = 0

for i in range(10):
    match = cass.get_match(base_id)

    if match.blue_team.win:
        print("%d Blue Team Wins!" % base_id)
        blue_wins += 1
    else:
        print("%d Red Team Wins!" % base_id)
        red_wins += 1

    time.sleep(1)
    base_id += 1 

print(match)