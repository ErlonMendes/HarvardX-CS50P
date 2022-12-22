def main():  # Aula Unit Tests inicia com este programa
    x = int(input("What's x? "))
    print("x square is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
