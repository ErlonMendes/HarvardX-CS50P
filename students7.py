students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
