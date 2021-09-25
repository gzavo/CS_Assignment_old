import csv 
import matplotlib.pyplot as plt

with open('./istherecorrelation.csv','r',newline='') as csvfile:
  
  # remove header if any
	has_header = csv.Sniffer().has_header(csvfile.read(1024))
	if has_header:
		csvfile.seek(0)
		next(csvfile)
    
  # read and plot data
	beers= csv.reader(csvfile,delimiter=';')
	fig, ax=plt.subplots()
	for beer in beers:
		ax.barh(beer[0],float(beer[2])/float(beer[1].replace(',','.')))
    
	ax.set_xlabel('Hectoliters per person per year')
	ax.set_ylabel('Years')
	plt.savefig('beer-plot.png', dpi=300)
	plt.show()
  
