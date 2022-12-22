students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):  # Agora sem o auxílio de uma função para
    # fornecer a chave
    print(f"{student['name']} is in {student['house']}")
