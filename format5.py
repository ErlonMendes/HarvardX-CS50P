import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)  # O ? depois do espaço diz que o padrão pode ter nenhuma ou uma
# ocorrência deste espaço, o que faz com que Mendes,Erlon também funcione.

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}!")
