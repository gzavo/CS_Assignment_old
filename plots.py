import pandas as pd
import matplotlib.pyplot as plt
import csv

my_data = pd.read_csv('./istherecorrelation.csv',delimiter=";")
# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(my_data.Year, my_data["NL Beer consumption [x1000 hectoliter]"], color="red", marker="o")
# set x-axis label
ax.set_xlabel("Year",fontsize=14)
# set y-axis label
ax.set_ylabel("NL Beer consumption [x1000 hectoliter]",color="red",fontsize=14)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(my_data.Year, my_data["WO [x1000]"],color="blue",marker="o")
ax2.set_ylabel("WO [x1000]",color="blue",fontsize=14)
plt.show()
# save the plot as a file
fig.savefig('Beerplot.jpg',
            format='jpeg',
            dpi=300,
            bbox_inches='tight')