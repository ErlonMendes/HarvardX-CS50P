def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)  # Reduziu o tamanho do código utilizando map para alterar os caracteres para
    # upper em uma só linha.
    print(*uppercased)


if __name__ == "__main__":
    main()
