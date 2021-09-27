import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('istherecorrelation.csv', sep = ';')
df["WO [x1000]"]=df["WO [x1000]"].str.replace(',','.')
df["WO [x1000]"]=pd.to_numeric(df["WO [x1000]"],errors = 'coerce')

fig, ax1 = plt.subplots()

x = df['Year']
y1 = df['WO [x1000]']
y2 = df['NL Beer consumption [x1000 hectoliter]']

color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(x, y1, color=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Beer consumption [x1000 hectoliter]', color=color)  # we already handled the x-label with ax1
ax2.plot(x, y2, color=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()

fig.savefig('Beer consumption and WO.jpg',
            format='jpeg',
            dpi=300,
            bbox_inches='tight')