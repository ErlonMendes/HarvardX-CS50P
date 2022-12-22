import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):  # ^ = Começa com, \w+ = pelo menos um caractere alfanumérico, @, \w+ = pelo
    # menos um caractere alfanumérico, \. = torna o ponto literalmente um ponto, não qualquer caractere do padrão,
    # edu, $ = Termina com o edu.
    print("Valid")
else:
    print("Invalid")
