import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

table = []
try:
    for arg in sys.argv[1:]:
        with open(arg) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append({"item": row[0], "small_price": row[1], "large_price": row[2]})
    print(tabulate(table, headers="firstrow", tablefmt="grid"), )
except FileNotFoundError:
    sys.exit("File does not exist")
