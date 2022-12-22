import re

url = input("URL: ").strip()
username = re.sub(r"https://twitter\.com/", "", url)  # Não esquecer que o primeiro campo é um padrão e que o ponto
# literal precisa do escape "\".
print(f"Username: {username}")
