with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())  # Mais pythonic
