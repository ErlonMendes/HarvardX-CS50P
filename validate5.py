import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):  # ^ = Começa com, [^@]+ = pelo menos um caractere exceto @, @, [^@]+ =
    # pelo menos um caractere exceto @, \. = torna o ponto literalmente um ponto, não qualquer caractere do padrão,
    # edu, $ = Termina com o edu. Vai impedir que um email como erlon@@@harvard.edu seja considerado válido.
    print("Valid")
else:
    print("Invalid")
