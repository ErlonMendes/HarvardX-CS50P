from calculator8 import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    else:
        print("2 square OK")
    if square(3) != 9:
        print("3 square was not 9")
    else:
        print("3 square OK")


if __name__ == "__main__":
    main()


# Há mais linhas de código para testar a função do que na função em si.
# Deve haver uma maneira melhor de fazer estes testes
