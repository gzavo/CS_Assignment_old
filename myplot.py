import matplotlib.pyplot as plt 
import csv
import pandas as pd

data = pd.read_csv('./istherecorrelation.csv',";")

fig,ax = plt.subplots()
beer = ax.plot(data["Year"],data['NL Beer consumption [x1000 hectoliter]'],color='yellow',label='Beer Consumption')
ax2=ax.twinx()
wo = ax2.plot(data["Year"],data['WO [x1000]'],color='black',label='WO Students')
ax.set_xlabel("Year")
ax.set_ylabel("NL Beer Consumption [x1000 hectoliter]")
ax2.set_ylabel("WO [x1000]")
ax.set_title("Is there a correlation?")
legs = wo+beer
labs = [l.get_label() for l in legs]
ax.legend(legs, labs, loc=0)
fig.savefig('Correlation.png',format='jpg',dpi=300)
plt.show()

