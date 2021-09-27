import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv("istherecorrelation.csv",delimiter=';')
print(list(df.columns))
figure(dpi=300)
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
plt.rc('font', size=6)
plt.rc('axes', titlesize=6)

plt.scatter(df['WO [x1000]'],df['NL Beer consumption [x1000 hectoliter],'])

plt.xlabel("The amount of WO students (*1000)")
plt.ylabel("The amount of beer comsumed every year")

plt.show()