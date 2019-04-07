import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import core
import random

sns.set()
# Data
df = pd.DataFrame(core.teams)

ax = plt.subplot(111)
plt.xlabel("Games played")
plt.ylabel("Position")
plt.xticks(range(1, core.total + 1))
plt.grid(1)
plt.title("Rugby Team Positions")
colors = {
    'Bath': 'blue',
    'Wasps': 'orange', 
    'Leicester': 'green', 
    'Gloucester': 'red', 
    'Bristol': 'purple', 
    'Newcastle': 'brown',
    'Harlequins': 'pink',
    'Sale': 'gray',
    'Worcester': 'cyan', 
    'Northampton': 'teal',
    'Saracens': 'black',
    'Exeter': 'goldenrod'
}

for key, item in core.teams.items():
    if key == 'x':
        continue
    else: 
        ax.plot('x', '{}'.format(key), color=colors[key], data=df, marker='o')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.show()