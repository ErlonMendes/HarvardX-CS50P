def meow(n: int):  # : int is a type hint
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)
# Malan executou mypy meows3.py no Terminal
