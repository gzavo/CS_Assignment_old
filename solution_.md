## Question 1
Titles of papars that are *pivotal* to our knowledge:
 - MCC Van Dyke et al., 2019, Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens.
 - JT Harvey, Applied Ergonomics, 2002. An analysis of the forces required to drag sheep over various surfaces.
 - DW Ziegler et al., 2005, Reading Acquisition, Developmental Dyslexia, and Skilled Reading Across Languages: A Psycholinguistic Grain Size Theory.

## Question 2
Here we look at the data from *istherecorrelation.csv*. Below is given a scatter plot of the data, from which it appears that there is some positive correlation between the two variables. We can do further analysis by calculating the *Spearman correlation* for this data set which gives a value of 0.8 with a  *p*-value of 0.001. This makes sense, judging from the plot there appears to be a clear positive relation between beer consumption in the Netherlands and *WO*. Although it should be noted that the plot is a bit deceiving because of the scale of the *y*-axis. So perhaps some further research is needed to make an actual statement about this data.
![alt text](plot.png)

## Appendix A - Python code
```
import matplotlib.pyplot as plt
import csv

WO, beer = [], []

with open('istherecorrelation.csv', 'r') as file:
    file = csv.reader(file, delimiter=';')
    next(file)
    for row in file:
        temp = row[1].replace(',', '.')
        WO.append(float(temp))
        beer.append(float(row[2]))

plt.figure()
plt.xlabel('WO (x1000)')
plt.ylabel('NL beer consumption (x1000 hectoliter)')
plt.plot(WO, beer, marker='o', ls='')
plt.savefig('plot.png', dpi=300)
```