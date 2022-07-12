def main():
    num = get_number()
    meow(num)


def get_number():
    while True:
        n = int(input("How many meow's do you want? "))
        if n > 0:
            break
        else:
            print("You put an wrong value!")
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
# Parei em 35 minutos da aula
