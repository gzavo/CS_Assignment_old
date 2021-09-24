from typing import DefaultDict
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 300

# get a dataframe 
df_raw = pd.read_csv('istherecorrelation.csv',sep=';', decimal=",")
df = df_raw.rename(columns={'WO [x1000]': 'students', 'NL Beer consumption [x1000 hectoliter]': 'beer'})

# calculate hectoliters of beer per 1000 students
ratio = df["beer"]/df['students']
df["ratio"] = ratio

df.plot.scatter(x='students', y='beer')
plt.xlabel('Number of students (x1000)'); plt.ylabel('Beer consumption (x1000 hectoliter)')
plt.savefig('absolute.png')
plt.show()

df.plot.scatter(x='Year', y='ratio')
plt.xlabel('Year'); plt.ylabel('Ratio beer/students (hectoliter per student)')
plt.savefig('ratio.png')
plt.show()