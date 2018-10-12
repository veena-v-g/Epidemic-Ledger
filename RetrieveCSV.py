import csv

path = "Datasets/Mosquito/Zika/cdc_zika.csv";

br = "\n ---------- \n"

with open(path) as csvFile:
    reader = csv.reader(csvFile, delimiter=",")
    lines = 0
    confirmed = 0  # confirmed cases
    caseType = {

    }

    for row in reader:
        dataField = row[3]
        cases = row[7]

        if lines == 0:
            print(f"Column names are {', '.join}")
        elif dataField == "cumulative_confirmed_local_cases" and int(cases) > 0:
            print(f"Incident: {cases} confirmed case(s) in the {row[2]} of {row[1]} on {row[0]}")
            confirmed += int(cases)

        if dataField in caseType:
            caseType[dataField] += 1
        else:
            caseType[dataField] = 1

        lines += 1

    print(br)
    print("Data sets parsed: " + str(lines))
    print("Confirmed cases: " + str(confirmed))

    print(br)
    for i in caseType:
        print(i + " : " + str(caseType[i]))
