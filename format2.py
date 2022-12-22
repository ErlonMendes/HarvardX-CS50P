import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # Busca pelo padrão começa com um ou mais caracteres em grupo, vírgula,
# espaço e termina com um ou mais caracteres também em grupo

if matches:
    last, first = matches.groups()  # Os grupos definidos entre parênteses na quarta linha são armazenados
    # respectivamente em last e first
    name = f"{first} {last}"

print(f"Hello, {name}!")
