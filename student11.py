class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  # Variáveis name e house foram armazenadas no objeto Student seguindo a estrutura
    # da classe.
    return student


if __name__ == "__main__":
    main()
