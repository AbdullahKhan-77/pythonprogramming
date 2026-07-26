import csv

with open("sample_data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is a {row['age']}-year-old {row['role']} from {row['city']}")