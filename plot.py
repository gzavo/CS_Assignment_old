import matplotlib.pyplot as plt
import csv
import codecs


def read_csv(filename, data):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        line = 0
        headers = []
        for row in reader:
            if line == 0:
                for element in row:
                    headers.append(element.strip("\xef\xbb\xbf"))
                    data[element.strip("\xef\xbb\xbf")] = []
                line += 1
            else:
                for i, element in enumerate(row):
                    data[headers[i]].append(float(element.replace(',', '.')))            
    return headers, data


if __name__ == "__main__":
    # save data from csv file
    data = {}
    headers, data = read_csv("istherecorrelation.csv", data)

    # create figure
    fig, ax = plt.subplots()

    # plot data on separate y axes
    ax.plot(data[headers[0]], data[headers[1]], 'b-', label=f"{headers[1]}")
    ax.set_ylabel(headers[1], color='blue')

    ax2 = ax.twinx()
    ax2.plot(data[headers[0]], data[headers[2]], 'r-', label=f"{headers[2]}")
    ax2.set_ylabel(headers[2], color='red')
    ax.set_xlabel(headers[0])

    fig.savefig('plot.png', dpi=300, bbox_inches='tight')