# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:10:55 2021

@author: LPras
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('istherecorrelation.csv', delimiter=';')

#plt.plot(df1['Year'], df1['WO [x1000]'])

plt.figure(dpi=300)
plt.subplot(211)
plt.plot(df1['Year'], df1['NL Beer consumption [x1000 hectoliter]'], '-g')
plt.title('Beer consumption of WO students')
plt.ylabel('x1000 hectoliter')
plt.subplot(212)
plt.plot(df1['Year'], df1['WO [x1000]'], '-r')
plt.xlabel('Year')
plt.ylabel('WO students [x1000]')
plt.show()
