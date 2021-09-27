import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")

print(data)
year = data.iloc[:,0]
students = data.iloc[:,1]
beer = data.iloc[:,2]

fig, axs = plt.subplots(1,3,figsize=(18,8))
axs[0].plot(year, beer, 'ro')
axs[0].set_xlabel("Year", fontsize=14)
axs[0].set_ylabel("Beer consumption [x1000 hectoliter]", fontsize=14)
axs[0].set_title("Beer consumption of students", fontsize=14)

axs[1].plot(year, beer/students, 'go')
axs[1].set_xlabel("Year", fontsize=14)
axs[1].set_ylabel("Beer consumption per student [hectoliter]", fontsize=14)
axs[1].set_title("Average beer consumption of a student", fontsize=14)

fig.suptitle("Dutch WO student beer consumption increasing or not?", fontsize=16)

axs[2].plot(students, beer, 'yo')
axs[2].set_xlabel("Number of students [x1000]", fontsize=14)
axs[2].set_ylabel("Beer consumption [x1000 hectoliters]", fontsize=14)
axs[2].set_title("Beer consumption vs students", fontsize=14)
plt.tight_layout()
plt.savefig("correlationquestion.png")
plt.show()