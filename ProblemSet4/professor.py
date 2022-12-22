import random


def main():
    n = get_level()
    while True:
        e = 0
        score = 0
        i = 1
        x = generate_integer(n)
        y = generate_integer(n)
        while i <= 10:
            try:
                print(f"{x} + {y} = ", end="")
                r = int(input())
                if r == x + y:
                    score = score + 1
                    x = generate_integer(n)
                    y = generate_integer(n)
                    i = i + 1
                else:
                    e = e + 1
                    print("EEE")
                    pass
                    if e > 2:
                        print(f"{x} + {y} = {x + y}")
                        x = generate_integer(n)
                        y = generate_integer(n)
                        i = i + 1
                        e = 0
            except ValueError:
                print("EEE")
                pass
        print(f"Score: {score}")
        break


def get_level():
    level = input("Level: ")
    if level.isalpha() or int(level) <= 0 or int(level) > 3:
        input("Level: ")
    else:
        level = int(level)
        for i in [1, 2, 3]:
            if level == i:
                return level


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
