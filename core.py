import os
import json

PATH = '/Users/ed/Projects/rugby_visualiser/rugby_data/'
FILE_NAMES = os.listdir(PATH)

file_list = sorted([item for item in FILE_NAMES])

def create_axis(file_list, feature):
    teams = {
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
    for item in file_list:
        with open(PATH + item, 'r') as jsonfile:
            jsonreader = json.load(jsonfile)
            for item in jsonreader:
                for team in teams:
                    if item['Team'] == team:
                        teams[team].append(int(item[feature]))
    x = [x for x in range(1, len(file_list) + 1)]
    teams['x'] = x
    return teams

teams = create_axis(file_list, 'Points')