phrase = input("Input: ").strip().split()
vowels = "a e i o u A E I O U"
print("Output: ", end="")
for word in phrase:
    for vowel in vowels:  # Busca as vogais e as substitui por nada
        if word.find(vowel) != -1:
            word = word.replace(vowel, "")
    print(word, end=" ")
