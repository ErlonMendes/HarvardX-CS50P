import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):  # ^ = Começa com, \w+ = pelo menos um caractere
    # alfanumérico, @, (\w+\.) = pelo menos um caractere alfanumérico e ponto, ? = padrão ou grupo de padrões que
    # acabou de ser definido pode aparecer uma ou nenhuma vez, \w+ = pelo menos um caractere alfanumérico,
    # \. = torna o ponto literalmente um ponto, não qualquer caractere do padrão, edu, $ = Termina com o edu.
    # re.IGNORECASE é um flag que faz no re o que faziamos com .lower() na entrada do email.
    print("Valid")
else:
    print("Invalid")
