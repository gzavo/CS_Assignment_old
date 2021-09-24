import pandas as pd
import matplotlib.pyplot as plt


# get data
data = pd.read_csv('./istherecorrelation.csv', delimiter=";")

fig,ax = plt.subplots()  # create figure and axis objects with subplots()
ax.plot(data.Year, data["NL Beer consumption [x1000 hectoliter]"], color='green', marker='*')  # make first plot
ax.set_title('Is there a correlation?')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("NL Beer consumption [x1000 hectoliter]", color='green', fontsize=12)
ax2=ax.twinx()  # twin object for two different y-axis on the sample plot
ax2.plot(data.Year, data["WO [x1000]"], color='blue')  # make second plot
ax2.set_ylabel("WO [x1000]", color='blue', fontsize=12)  # second y axis
plt.show()
fig.savefig('Beerconsumption.jpg', format='jpeg', dpi=300, bbox_inches='tight')  # save plot