import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import core
import random

sns.set()
# Data
df = pd.DataFrame(core.teams)

fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(111)
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
plt.legend(loc='center right', bbox_to_anchor=(1.4, 0.5))

# plt.show()

fname = 'points.png'
plt.savefig(fname, dpi=300, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None)