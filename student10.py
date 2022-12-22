class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")  # Funcionou, agora como class. No entanto, parece faltar alguma
    # coisa nos "...", pois o PyCharm apresenta um alerta.


def get_student():
    student = Student()  # Esta linha criou um objeto para a classe.
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
