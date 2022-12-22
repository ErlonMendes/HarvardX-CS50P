import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):  # ^ = Começa com, .+ = pelo menos um caractere, @, .+ = pelo menos um
    # caractere, \. = torna o ponto literalmente um ponto, não qualquer caractere do padrão, edu, $ = Termina com o
    # edu.
    print("Valid")
else:
    print("Invalid")
