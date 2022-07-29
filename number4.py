try:
    x = int(input("Who's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
# O NameError acaba.
