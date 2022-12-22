import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):  # O walrus operator ":=", operador morsa em português, que combina o
    # if com o armazenamento da resposta na variável.
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}!")
