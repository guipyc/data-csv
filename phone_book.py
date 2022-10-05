import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)
    for row in reader:
        print(row["first_name"],row["last_name"],row["phone_number"])

print(type(row))
