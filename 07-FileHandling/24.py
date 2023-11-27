import csv

with open("students_list.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = int(row['age'])
        if age < 30:
            print(f"{row['first_name']}   {row['last_name']}   {row['email']}")
