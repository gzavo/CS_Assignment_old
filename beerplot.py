import csv 
import matplotlib.pyplot as plt

with open('./istherecorrelation.csv','r',newline='') as csvfile:
	
	# ignore header if any
	has_header = csv.Sniffer().has_header(csvfile.read(1024))
	if has_header:
		csvfile.seek(0)
		next(csvfile)
		
	# read data and plot
	beers= csv.reader(csvfile,delimiter=';')
	fig, ax=plt.subplots(1,2,figsize=(10,6))
	for beer in beers:
		ax[0].scatter(float(beer[2]),float(beer[1].replace(',','.')))
		ax[1].barh(beer[0],float(beer[2])/float(beer[1].replace(',','.')))

	ax[0].set_xlabel('WO students x1000')
	ax[0].set_ylabel('hectoliters x1000')
	ax[0].grid() 
	ax[1].set_xlabel('Hectoliters per person per year')
	ax[1].set_ylabel('Years')
	# save image
	plt.savefig('beer-plot.png', dpi=300)
	plt.show()
