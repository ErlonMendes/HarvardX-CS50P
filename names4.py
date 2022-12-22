name = input("What's your name? ")
file = open("names.txt", "a")  # O argumento "a" adiciona novos nomes ao arquivo
file.write(f"{name}\n")
file.close()
