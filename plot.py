import matplotlib.pyplot as plt
import csv

year_list = []
beer_list = []
wo_list = []

with open('istherecorrelation.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        year_list.append(int(row[0]))
        wo = row[1].replace(',', '.')
        wo_list.append(wo)
        beer_list.append(int(row[2]))

plt.plot(year_list, wo_list)
plt.show()
plt.plot(year_list, beer_list)
plt.show()