import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

db = pd.read_csv("istherecorrelation.csv", sep=';')


fig, ax = plt.subplots(dpi=300)
ax.plot(db['WO [x1000]'], db['NL Beer consumption [x1000 hectoliter]'])

ax.set(xlabel='WO [x1000]', ylabel='NL Beer consumption [x1000 hectoliter]',
       title='WO vs Beer consumption in the Netherlands')
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(6)
ax.grid()

fig.savefig("correlation.png")
plt.show()