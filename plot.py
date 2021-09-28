# Import libraries
import csv
import matplotlib.pyplot as plt

# Open en store the csvfile
with open('istherecorrelation.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ';')
    next(csvreader)
    years = []
    WO = []
    beer = []
    for row in csvreader:
        years.append(row[0])
        WO.append(row[1])
        beer.append(row[2])

# Make the plot
plt.title("Beer consumption and number of WO students over the years")
plt.plot(years, WO, label = "WO")
plt.plot(years, beer, label = "beer")
plt.xlabel('Years')
plt.ylabel('Amount WO students and beer consumption')
plt.legend()
plt.savefig('plot.png', dpi = 300)
plt.show()
