import csv
import matplotlib.pyplot as plt

with open('istherecorrelation.csv') as file:
    csvreader = csv.reader(file, delimiter=";")
    header = []
    header = next(csvreader)
    header[0] = header[0][1:]
    rows = []
    for row in csvreader:
        rows.append(row)

years = []
wo = []
beer = []
for row in rows:
    years.append(row[0])
    wo.append(row[1])
    beer.append(row[2])

plt.plot(years, wo, label = "wo")
plt.plot(years, beer, label = "beer")
plt.xlabel('years')
plt.legend()
plt.savefig('plot.png', dpi=300)
plt.show()
