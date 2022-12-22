def main():
    name = input("camelCase: ").strip()
    alphabet_list = alphabet()
    for letter in alphabet_list:  # Busca as letras maiúsculas do modo camelCase e substitui por _letra
        if name.find(letter) != -1:
            name = name.replace(letter, "_" + letter.lower())
    print(f"snake_case: {name}")


def alphabet():  # Cria uma lista com as letras maiúsculas do alfabeto
    from string import ascii_uppercase
    return list(ascii_uppercase)


if __name__ == "__main__":
    main()
