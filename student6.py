def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]  # Com [] get_student retorna um list e não um tuple, aceitando a alteração de student Padma.


if __name__ == "__main__":
    main()
