students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}  # Três linhas de comando anteriores em uma
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
