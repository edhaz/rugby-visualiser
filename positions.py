import matplotlib.pyplot as plt
import pandas as pd
import core
import random

# Data
df = pd.DataFrame(core.teams)


ax = plt.subplot(111)
plt.xlabel("Games played")
plt.ylabel("Position")
plt.yticks(range(13))
plt.grid(1)
plt.title("Rugby Team Positions")
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'teal', 'black', 'goldenrod']
for key, item in core.teams.items():
    if key == 'x':
        continue
    else: 
        color = random.choice(colors)
        colors.remove(color)
        ax.plot('x', '{}'.format(key), color=color, data=df, marker='o')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.show()