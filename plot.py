"""
Plot of 'istherecorrelation.csv'. 
Source code plot from matplotlib.org (parasite simple)
"""
import pandas as pd
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt

# opens file and gets columns
df = pd.read_csv("istherecorrelation.csv",sep=';')
index = df[df.columns[0]].tolist()
WO = df[df.columns[1]].tolist()
Beer = df[df.columns[2]].tolist()

host = host_subplot(111)
par = host.twinx()

# adds labels
host.set_xlabel("Years")
host.set_ylabel("WO")
par.set_ylabel("Beer")

# add plots together
p1, = host.plot(index, WO, label="WO [x1000]")
p2, = par.plot(index, Beer, label="NL Beer consumption [x1000 hectoliter]")

leg = plt.legend()

# colour WO labels blue
host.yaxis.get_label().set_color(p1.get_color())
leg.texts[0].set_color(p1.get_color())

# colour Beer labels yellow
par.yaxis.get_label().set_color(p2.get_color())
leg.texts[1].set_color(p2.get_color())

plt.savefig('plot.png',dpi=300)
plt.show()