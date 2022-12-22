import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")

students = []
try:
    with open(sys.argv[1], "r") as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            name = row["name"].split(', ')
            first = name[1]
            last = name[0]
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline='') as file2:
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in students:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
