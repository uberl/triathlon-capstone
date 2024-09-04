import csv
import json

with open("list.json", "r") as file:
    raw_data = json.load(file)

    data = [
        {
            "bib": d[0],
            "team": d[5],
            "place": d[1].replace(".", ""),
            "name": d[3],
            "nationality": d[4],
            "swim_time": d[6].split(" ")[0],
            "swim_place": d[6].split(" ")[-1].replace(".", ""),
            "t1_time": d[7],
            "bike_time": d[8].split(" ")[0],
            "bike_place": d[8].split(" ")[-1].replace(".", ""),
            "t2_time": d[9],
            "run_time": d[10].split(" ")[0],
            "run_place": d[10].split(" ")[-1].replace(".", ""),
            "total_time": d[11],
        }
        for d in raw_data["data"]["#2_Frauen"]
    ]

    # CSV file path
    csv_file = "data.csv"

    # Open the file in append mode
    with open(csv_file, "a", newline="") as file:
        # Get the fieldnames from the first dictionary
        fieldnames = data[0].keys()

        # Create a DictWriter object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the data (without writing the header again)
        writer.writerows(data)

    print("Data appended successfully!")
