import numpy as np
import csv


def get_five_num_summ(data):

    numpy_array = np.array(data)

    list.sort(data)

    # Get minimum
    m = data[0]

    # Get first quartile
    Q1 = np.percentile(data, 25)

    # Get median
    Q2 = np.percentile(data, 50)

    # Get third quartile
    Q3 = np.percentile(data, 75)

    # Get maximum
    M = np.percentile(data, 25)

    return [m, Q1, Q2, Q3, M]


def get_statistics_country(country,index):
    with open('../Datasets/Mosquito/Zika/cdc_zika.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        summary = {}
        for row in reader:
            list = row[0].split(",")
            if len(list) >= index and str.startswith(list[1], "\"" + country):
                type = list[index]
                if type in summary:
                    if len(list) >= 8 and list[8] == "cases":
                        summary[type] += list[7]
                else:
                    summary[type] = list[7]

        return summary

summary = get_statistics_country("Argentina",3)
print("Statistics for Argentina")
for key in summary:
    print(key + ": " + str(summary[key]))