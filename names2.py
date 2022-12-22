name = input("What's your name? ")
file = open("names.txt", "w")  # O argumento "w" irá criar arquivo novo sempre que este comando é executado
file.write(name)
file.close()
