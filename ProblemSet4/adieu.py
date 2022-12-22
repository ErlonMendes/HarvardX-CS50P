n = list()
while True:
    try:
        n.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to ", end="")
        for name in n:
            if len(n) == 1:
                print(f"{name}")
            elif len(n) == 2:
                print(f"{n[0]} and {n[1]}")
                break
            elif name == n[-1]:
                print(f"and {n[-1]}")
            else:
                print(f"{name}, ", end="")
        break
