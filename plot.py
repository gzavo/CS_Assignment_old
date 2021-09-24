import matplotlib.pyplot as plt
import csv
from scipy import optimize
import numpy as np

year_list = []
beer_list = []
wo_list = []

with open('istherecorrelation.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        year_list.append(int(row[0]))
        wo = row[1].replace(',', '.')
        wo_list.append(float(wo))
        beer_list.append(int(row[2]))

def linear_function(x, a, b):
    return a * x + b

solution, covariance = optimize.curve_fit(linear_function, year_list, wo_list)

error = np.sqrt(np.diag(covariance))



x = np.arange(2006, 2022)
y = linear_function(x, 5.9027, -11635)

print(f"a = 5.9 +/- 0.3, b = -1.16e+04 +/- 6e+02")
print(f"The expected amount of students in 2021 is {y[-1]*1000:.0f}")
plt.plot(x, y)
plt.plot(year_list, wo_list)
plt.title('Amount of students from 2006 to 2018')
plt.xlabel('Year')
plt.ylabel('Amount of students (x1000)')
plt.xlim(2006, 2021)
plt.savefig('istherecorrelation.png')
