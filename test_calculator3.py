from calculator8 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square was not 9")


if __name__ == "__main__":
    main()
