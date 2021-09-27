import numpy as np
data = numpy.genfromtxt('isthecorrelation.csv', delimiter=',', names= 'WO [x1000]' , 'NL Beer consumption [x1000 hectoliter]')
plt.plot(data['WO [X1000'], data['NL Beer consumption [x1000 hectoliter]'], DPI = 300)
