import matplotlib.pyplot as plt
import csv

with open ('istherecorrelation.csv') as f:
    reader = csv.reader(f, delimiter=';')
    head = next(reader)
    year = []
    wo_students = []
    beer = []
    for row in reader:
        year.append(int(row[0]))
        wo_students.append(float(row[1].replace(',','.')))
        beer.append(float(row[2].replace(',','.')))
    print(year, wo_students)

    fig, ax = plt.subplots()
    ax.plot(year, wo_students, linestyle='-', marker='.', color='red', label='WO Students')
    ax.set_xlabel('Time in years')
    ax.set_ylabel('WO Students (x1000)', color='red')

    ax2 = ax.twinx()
    ax2.set_ylabel('Beer Consumption (x1000 HL)', color='blue')
    ax2.plot(year, beer, linestyle='-', marker='.', label='Beer Consumption', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    plt.show()