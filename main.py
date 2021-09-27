import matplotlib.pyplot as plt

def main():

    # Extract data from csv file using 'utf-8-sig' encoding, this removes
    # the strange characters at the start of the csv.
    # https://stackoverflow.com/questions/34399172/why-does-my-python-code-print-the-extra-characters-%C3%AF-when-reading-from-a-tex/34399309 
    with open("istherecorrelation.csv", encoding="utf-8-sig") as f:
        
        header = f.readline().strip().split(";")

        data = [row.strip().split(";") for row in f]

    # Store each column in a seperate list and convert the data type
    years = [int(row[0]) for row in data]
    wo = [float(row[1].replace(",", ".")) for row in data]
    beer_consumption = [float(row[2]) for row in data]

    fig, ax = plt.subplots()
    
    ax.set_xlabel(header[0])

    ax.plot(years, wo, '-ro', label=header[1])
    ax.set_ylabel(header[1])

    # Create a secondary y axis
    ax2 = ax.twinx()
    ax2.plot(years, beer_consumption, '-bo', label=header[2])
    ax2.set_ylabel(header[2])
    
    fig.legend()

    # Increase the figure size, such that the second yaxis label can be read
    fig.set_size_inches(10, 6)

    fig.savefig("plot.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
