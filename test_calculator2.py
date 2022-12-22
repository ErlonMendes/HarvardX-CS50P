from calculator8 import square


def main():
    test_square()


def test_square():
    assert square(2) == 4  # Alternativa para testes, mais compacta e sem if's
    assert square(3) == 9


if __name__ == "__main__":
    main()
