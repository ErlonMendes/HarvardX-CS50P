def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    return {"name": input("Name: "), "house": input("House: ")}


if __name__ == "__main__":
    main()
