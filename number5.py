while True:
    try:
        x = int(input("Who's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
# Repete a pergunta até que o usuário forneça um valor adequado.
