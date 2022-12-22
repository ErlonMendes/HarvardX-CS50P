class Wizard:  # Esta etapa explora o problema da variável name, que está presente nas classes Student e Professor
    # com linhas de comando idênticas. Como ambos são Wizard, esta classe pode unificar as coisas.
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):  # Student é uma classe da Wizard superclasse.
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):  # Professor é uma classe da Wizard superclasse.
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
