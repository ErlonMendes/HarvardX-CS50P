students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Revenclaw"}
]

houses = set()  # A classe set() é uma alternativa que elimina automaticamente os registros duplicados
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
