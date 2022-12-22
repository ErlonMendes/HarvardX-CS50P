def main():
    phrase = input("Input: ").strip().split()
    print("Output: ", end="")
    for word in phrase:
        print(shorten(word), end=" ")


def shorten(word):
    vowels = "a e i o u A E I O U"
    for vowel in vowels:  # Busca as vogais e as substitui por nada
        if word.find(vowel) != -1:
            word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
