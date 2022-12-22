def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # Interessante ver o efeito com e sem o *.


if __name__ == "__main__":
    main()
