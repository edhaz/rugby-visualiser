import os
import json

PATH = '/Users/ed/Projects/rugby_visualiser/rugby_data/'
FILE_NAMES = os.listdir(PATH)
teams = {
    'x': [x for x in range(1, 18)],
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

total = 0
file_names_sorted = []
for item in FILE_NAMES:
    file_names_sorted.append(item)
file_names_sorted = sorted(file_names_sorted)

for item in file_names_sorted:
    with open(PATH + item, 'r') as jsonfile:
        total += 1
        jsonreader = json.load(jsonfile)
        for item in jsonreader:
            for team in teams:
                if item['Team'] == team:
                    teams[team].append(int(item['Place']))

for key, val in teams.items():
    if len(val) != total:
        amount = total - len(val)
        val.extend(['12' for x in range(amount)])