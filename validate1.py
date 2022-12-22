email = input("What's your email? ").strip()

if "@" and "." in email:
    print("Valid")
else:
    print("Invalid")
# Obviamente não é um bom parâmetro para validar um e-mail
