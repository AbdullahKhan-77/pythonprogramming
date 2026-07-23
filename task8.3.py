import csv

engineer_count = 0
ages = []

with open("sample_data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["role"] == "Engineer":
            engineer_count += 1
        ages.append(int(row["age"]))

average_age = sum(ages) / len(ages)

print(f"Number of Engineers: {engineer_count}")
print(f"Average age: {average_age:.1f}")