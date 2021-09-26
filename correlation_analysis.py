#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./istherecorrelation.csv", sep=";", decimal=",")
data = data.set_index("Year", drop=True)

data.head()
# %%
plt.plot(data, "o")
#%%
data.describe()

# %%
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.grid()
p1 = ax.plot(data["WO [x1000]"], 'bo', label=data.columns[0])
p2 = ax2.plot(data["NL Beer consumption [x1000 hectoliter]"], 'go', label=data.columns[1])
lines = p1+ p2
ax.legend(lines, [data.columns[0],data.columns[1]])
_ = plt.title("Correlation plot between WO and Beer consumption")
plt.savefig(DPI=300, fname="thereiscorrelation")
