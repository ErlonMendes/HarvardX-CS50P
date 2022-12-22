import random

while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
            pass
        elif guess < number:
            print("Too small!")
            pass
        else:
            print("Just right!")
            break
    except ValueError:
        pass
