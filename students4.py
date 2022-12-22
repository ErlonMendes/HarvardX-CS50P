students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}  # Um dicionário
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
