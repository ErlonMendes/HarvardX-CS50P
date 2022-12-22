def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {"name": input("Name: "), "house": input("House: ")}  # Monta um dict.
    return student


if __name__ == "__main__":
    main()
