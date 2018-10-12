import csv

path = "Datasets/Mosquito/Zika/cdc_zika.csv";
br = "\n ---------- \n"

br = "\n ---------- \n"

with open(path) as csvFile:
    reader = csv.reader(csvFile, delimiter=",")
    lines = 0
    confirmed = 0  # confirmed cases
    caseType = {}
    region = {}
    date = {}

    }

    for row in reader:
        dataField = row[3]
        cases = row[7]
        location = row[1]  # .split("-", 1)[0]
        time = row[0]

        if lines == 0:
            print(f"Column names are {', '.join}")
        elif dataField == "zika_confirmed_laboratory" or dataField == "zika_confirmed_clinic":
            if cases != "NA" and int(cases) > 0:
                # print(f"Incident: {cases} confirmed case(s) in the {row[2]} of {location} on {time}")
                confirmed += int(cases)

                if location in region:
                    region[location] += int(cases)
                else:
                    region[location] = int(cases)

                if time in date:
                    date[time] += int(cases)
                else:
                    date[time] = int(cases)

        if dataField in caseType:
            caseType[dataField] += 1
        else:
            caseType[dataField] = 1

        lines += 1

    print(br)
    print("Total line count: " + str(lines))
    print("Relevant data sets parsed: "
          + str(caseType["zika_confirmed_laboratory"] + caseType["zika_confirmed_clinic"]))
    print("Confirmed cases: " + str(confirmed))

    print(br)

    miscRegion = 0

    for i in region:
        if region[i] > 10:
            print(i + " : " + str(region[i]))
        else:
            miscRegion += region[i]
    print("Other region : " + str(miscRegion))

    print(br)

    for i in date:
        print(i + " : " + str(date[i]))

    print(br)

    miscType = 0

    for i in caseType:
        if caseType[i] > 100:
            print(i + " : " + str(caseType[i]))
        else:
            miscType += caseType[i]
    print("Other data type : " + str(miscType))

