import matplotlib.pyplot as plt
import csv
import pandas as pd

# data = []
# print(data)
# with open('istherecorrelation.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#         data += [row]
#         print(row)
# print(data)

df = pd.read_csv('istherecorrelation.csv', delimiter=';')
print(df)
print(df.info())
fig = plt.figure(dpi=300)

df.plot(y="WO [x1000]", x="Year", kind="scatter", ax = plt.gca())
plt.show()