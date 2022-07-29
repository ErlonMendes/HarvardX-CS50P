try:
    x = int(input("Who's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
# Malan introduz o try and except, para lançar uma mensagem em caso de erro do usuário
