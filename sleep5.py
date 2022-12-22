def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i  # yield faz a entrega parcial dos dados solicitados nesta função.


if __name__ == "__main__":
    main()
# Agora o programa roda com 1000000 ovelhas.
