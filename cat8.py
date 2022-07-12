while True:
    n = int(input("How many meow's do you want? "))
    if n > 0:
        break  # Introduziu o break, conclui o loop
    else:
        print("You put an wrong value!")

for _ in range(n):
    print("meow")
