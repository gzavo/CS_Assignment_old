import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/filippos/Documents/istherecorrelation.csv', delimiter=',')
print (data)

fig,ax = plt.subplots()

Graph = ax.plot(data["Year"],data['NL Beer consumption [x1000 hectoliter]'],color='red',label='Beer Consumption')
ax2=ax.twinx()
WO = ax2.plot(data["Year"],data['WO [x1000]'],color='blue',label='WO Students')
ax.set_xlabel("Year")
ax.set_ylabel("NL Beer Consumption [x1000 hectoliter]")
ax2.set_ylabel("WO [x1000]")
ax.set_title("Correlation possible?")

legend = WO+Graph
label = [l.get_label() for l in legend]
ax.legend(legend, label, loc=0)


ax.grid()
fig.savefig('Correlation.png',format='jpg',dpi=300)
plt.show()