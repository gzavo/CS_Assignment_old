import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


data1 = pd.read_csv("/Users/Senne/Documents/Senne Bakker/UVA:VU/Seminar/Assignment lec 3/CS_Assignment/istherecorrelation.csv",delimiter=";")

years = data1.iloc[:,0]
# Number of students in terms of thousands
wo = data1.iloc[:,1]
print(wo)
# Beer consumptions in terms of thousands of hectoliters
beer_cons = data1.iloc[:,2]
ratio = []

# convert data
for i in range(len(beer_cons)):
    wo[i] = wo[i].replace(',', '.', 1)
    wo[i] = float(wo[i])

    ratio.append(beer_cons[i]/wo[i])


# plot data
# plt.scatter(years, ratio)
plt.scatter(years, beer_cons)
plt.title("Total beer consumption over the years")
plt.xlabel("Years")
plt.ylabel("Consumption (10^3 hl)")
plt.show()