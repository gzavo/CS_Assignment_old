import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('istherecorrelation.csv', delimiter=";")

fig, ax = plt.subplots(figsize=(6,6), dpi=300)

ax.plot(data['Year'], data['WO [x1000]'], label="WO [x1000]")

ax2 = ax.twinx()
ax2.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], label="NL Beer consumption [x1000 hectoliter]", color="red")
ax.legend(loc=1)
ax2.legend(loc=0)
plt.savefig("correlation")
plt.show()
