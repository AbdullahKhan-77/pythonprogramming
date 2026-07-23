import csv

with open("sample_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        