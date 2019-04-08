import os
import json
import re

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
    x_axis = []
    date_regex = re.compile(r'(\d+)-(\d+)-(\d+)')
    
    for item in file_list:
        found = date_regex.search(item).group()
        x_axis.append((str(found)))

        with open(PATH + item, 'r') as jsonfile:
            jsonreader = json.load(jsonfile)
            for item in jsonreader:
                for team in teams:
                    if item['Team'] == team:
                        teams[team].append(int(item[feature]))

    teams['x'] = x_axis
    return teams

teams = create_axis(file_list, 'Points')