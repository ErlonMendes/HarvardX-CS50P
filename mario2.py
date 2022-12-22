def main():
    height = int(input("Height: "))
    piramid(height)


def piramid(n):  # Basicamente, há um problema que queremos resolver. A pirâmide tem sempre n-1 de altura.
    for i in range(n):
        print(i, end=" ")  # Esta linha investiga o valor de i. O end=" " impede a criação de uma nova linha.
        print("#" * (i+1))  # A minha solução foi usar i+1 em vez de i nesta linha. David Malan sugere a mesma solução
        # em seguida.


if __name__ == "__main__":  # Foi usado da aula Libraries (Bibliotecas). Só executa o main caso o próprio programa seja
    # executado.
    main()
