# Aula Unit Tests utiliza este programa em 38:10
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("Hello,", to)


if __name__ == "__main__":
    main()
