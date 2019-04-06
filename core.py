import os
import pandas as pd
import matplotlib.pyplot as plt

PATH = '/Users/ed/Projects/rugby_visualiser/rugby_data/'

file_names = os.listdir(PATH)
print(file_names)
file_names = [file for file in file_names if '.csv' in file]
print(file_names)

for file in file_names:
    df = pd.read_csv(PATH + file, index_col = 0)
    plt.plot(df)

plt.show()