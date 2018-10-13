import numpy as np
import csv
from numpy import percentile
from numpy import array


def get_five_num_summ(numbers):

    for index in range(len(numbers)):
        numbers[index] = int(numbers[index].replace("\"", ""))
        print(type(numbers[index]))

    list.sort(numbers)

    # Get minimum
    m = numbers[0]

    # Get maximum
    M = numbers[len(numbers) - 1]

    numbers = np.asarray(numbers)
    # Get 1st, 3rd quartiles and median
    quartiles = percentile(numbers, [25, 50, 75])
    five_num_summary = [m]
    five_num_summary += list(quartiles)
    five_num_summary += [M]

    return five_num_summary


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


def get_world_summary():
    countries = []
    world_summary = {}
    with open('../Datasets/Mosquito/Zika/cdc_zika.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            list = row[0].split(",")
            if len(list) > 1:
                country = list[1][1:list[1].find("-")]
                if country not in countries and country != "location":
                    countries.append(country)

        for country in countries:
            # print(country)
            country_summary = get_statistics_country(country, 3)
            for case in country_summary:
                if "confirmed" in case or "probable" in case:
                    if country in world_summary:
                        world_summary[country] += country_summary[case]
                    else:
                        world_summary[country] = country_summary[case]
        return country_summary;


summary = get_world_summary()
print(str(get_five_num_summ(list(summary.values()))))
