import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):  # .+ = pelo menos um caractere, @, .+ = pelo menos um caractere, \. = torna o
    # ponto literalmente um ponto, não qualquer caractere do padrão, edu. O "r" vem de raw.
    print("Valid")
else:
    print("Invalid")
