import re

url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)  # Agora funciona com https ou http. Tolerante a
# presença ou não do "www". O grupo https:// e sua variante tornam-se opcionais.
print(f"Username: {username}")
