import csv

path = "Datasets/Mosquito/Zika/cdc_zika.csv";

with open(path) as csvFile:
    reader = csv.reader(csvFile, delimiter=",")
    lines = 0

    for row in reader:
        if lines == 0:
            print(f"Column names are {', '.join}")
        else:
            print(f"Incident: on {row[0]} in the {row[2]} of {row[1]}")

        lines += 1

    print("Line count: " + str(lines))
