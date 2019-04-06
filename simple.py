import ijson
import pandas as pd
import matplotlib.pyplot as plt


filename = "rugby_table.json"
data = []
with open(filename, 'r') as f:
    objects = ijson.items(f, 'item')
    columns = list(objects)
    # column_names = [key for key in columns]
    column_names = [list(i.keys()) for i in columns[:1]]
    column_names = column_names[0]
    for row in columns:
        current_row = []
        for item in row.values():
            current_row.append(item)
        data.append(current_row)

# print(column_names)
# for item in data:
#     print(item)

teams = pd.DataFrame(data, columns=column_names)
print(teams)
