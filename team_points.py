import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from core import teams

sns.set()
df = pd.DataFrame(teams)

fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(111)
plt.title("Rugby Premiership Points")
plt.xlabel("Dates of games played")
plt.ylabel("Points")
plt.xticks(range(len(teams['x'])), rotation=90)
plt.grid(1)
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

for key, item in teams.items():
    if key == 'x':
        continue
    else: 
        ax.plot('x', '{}'.format(key), color=colors[key], data=df, marker='o')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='center right', bbox_to_anchor=(1.4, 0.5), title="Teams")

# plt.show()

fname = 'points.png'
plt.savefig(fname, dpi=300, bbox_inches='tight')