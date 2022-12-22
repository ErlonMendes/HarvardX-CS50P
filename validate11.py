import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:["
             r"a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):  # O padrão oficial
    print("Valid")
else:
    print("Invalid")
