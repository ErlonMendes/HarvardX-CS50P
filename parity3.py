def main():
    num = int(input("Type a number: "))
    if is_even(num):  # Está chamando uma expressão booleana, o que confirma a condição do if (interessante)
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


def is_even(x):
    return True if x % 2 == 0 else False  # Agora em uma única linha


main()
