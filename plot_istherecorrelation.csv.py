import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("istherecorrelation.csv", delimiter=";")
df.columns
df['WO [x1000]'] = df['WO [x1000]'].apply(lambda x: x.replace(',', '.'))
df['WO [x1000]'] = df['WO [x1000]'].map(float)

fig,ax = plt.subplots()
# make a plot
ax.plot(df["Year"], df['WO [x1000]'], color="red", marker="o")
# set x-axis label
ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("WO (x1000)", color="red", fontsize=12)
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(df["Year"], df['NL Beer consumption [x1000 hectoliter]'],color="blue",marker="o")
ax2.set_ylabel('NL Beer consumption (x1000 hl)',color="blue",fontsize=12)
plt.title("Is there correlation?", fontsize=14)
plt.savefig("data-plot.jpg", dpi=300, bbox_inches = "tight")
plt.show()


