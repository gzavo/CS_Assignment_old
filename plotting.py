import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data
df = pd.read_csv('istherecorrelation.csv', sep = ';')

x = df['WO [x1000]']
y = df['NL Beer consumption [x1000 hectoliter]']

x = list(map(lambda x:x.replace(',', '.'), x))
x = list(map(lambda x:float(x), x))
y = list(map(lambda x:float(x), y))

# fit trendline
a, b = np.polyfit(x, y, 1)
print(a)
print(b)

# scatterplot
plt.plot(x, y, 'bo', label = 'Data')

# plot trendline
xvals = [205, 280]
yvals = list(map(lambda x:a*x + b, xvals))
plt.plot(xvals, yvals, 'r-', label = 'Linear fit' )


plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')

plt.legend()
plt.title('WO students vs. Beer consumption in the Netherlands')
plt.show()
