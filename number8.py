def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("Who's x? "))
        except ValueError:
            pass  # Introduziu o comando pass


main()
