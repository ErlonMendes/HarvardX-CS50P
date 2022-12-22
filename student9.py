def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"  # Dict's também são mutáveis como list's.
    print(f"{student['name']} from {student['house']}")


def get_student():
    return {"name": input("Name: "), "house": input("House: ")}


if __name__ == "__main__":
    main()
