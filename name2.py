import sys
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
# No Terminal, David digita um comando equivalente ao python name2.py, sem um nome, para obter um IndexError,
# então o modifica com try and except
