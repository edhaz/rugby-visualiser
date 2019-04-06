import os
import json

PATH = '/Users/ed/Projects/rugby_visualiser/rugby_data/'
FILE_NAMES = os.listdir(PATH)
teams = {
    'x': [x for x in range(32)],
    'Exeter': [],
    'Sale': [],
    'Saracens': [],
    'Leicester': [],
    'Harlequins': [],
    'Gloucester': [],
    'Northampton': [],
    'Bath': [],
    'Wasps': [],
    'Bristol': [],
    'Worcester': [],
    'Newcastle':[]
}

for item in FILE_NAMES:
    with open(PATH + item, 'r') as jsonfile:
        jsonreader = json.load(jsonfile)
        for item in jsonreader:
            for team in teams:
                if item['Team'] == team:
                    teams[team].append(int(item['Place']))


for key, val in teams.items():
    if len(val) != 32:
        amount = 32 - len(val)
        val.extend(['12' for x in range(amount)])