import re

url = input("URL: ").strip()
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):  # Padrão semelhante ao
    # de antes, mas perceba o detalhe de colocar o nome do usuário em um grupo "(.+)". (?:...) não vai armazenar este
    # grupo em matches, permitindo que eu busque o usuário no grupo 1.
    print(f"Username: {matches.group(1)}")
else:
    print("Not a Twitter URL")
