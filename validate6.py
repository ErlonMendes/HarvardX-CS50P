import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):  # ^ = Começa com, [a-zA-Z0-9_]+ = pelo menos um
    # caractere nos intervalos definidos e _, @, [a-zA-Z0-9_]+ = pelo menos um caractere nos intervalos definidos e
    # _, \. = torna o ponto literalmente um ponto, não qualquer caractere do padrão, edu, $ = Termina com o edu.
    print("Valid")
else:
    print("Invalid")
