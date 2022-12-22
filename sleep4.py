def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
# O programa não roda com 1000000 ovelhas. MemoryError, dá uma merda desgraçada. Parou de rodar o vídeo, inclusive.
