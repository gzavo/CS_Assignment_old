import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats.stats import pearsonr

sns.set()
data = pd.read_csv(
    "/tmp/CS_Assignment/istherecorrelation.csv",
    sep=";",
    decimal=",",
    header=0,
    names=["year", "wo", "beer"],
)


print(pearsonr(data.beer, data.wo))
color = "tab:red"
fig, ax1 = plt.subplots(dpi=300, figsize=(12, 7))
ax1.tick_params(axis="y", labelcolor=color)
ax1.set_xlabel("Year")
ax1.set_ylabel("Beer comsumption in NL [x1000 hectoliters]", color=color)
ax1.plot(data.year, data.beer, c=color)

color = "tab:green"
ax2 = ax1.twinx()
ax2.tick_params(axis="y", labelcolor=color)
ax2.set_ylabel("Number of WO students [x1000]", color=color)
ax2.plot(data.year, data.wo, c=color)


plt.show()
