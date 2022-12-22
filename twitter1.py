url = input("URL: ").strip()
# O objetivo aqui é pegar apenas o username e ignorar o restante.
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
