def main():
    height = int(input("Height: "))
    piramid(height)


def piramid(n):  # Basicamente, há um problema que queremos resolver. A pirâmide tem sempre n-1 de altura.
    for i in range(n):
        print("#" * (i+1))  # Voltamos ao erro de antes para a apresentação de uma nova ferramenta, o debugger.


if __name__ == "__main__":
    main()
# Como o meu VS Code está em português, os botões de depuração mais importantes são Contornar (Step Over) e
# Intervir (Step Into). O Intervir vai executar passo a passo a linha selecionada, enquanto o Contornar vai
# executar toda a função de uma só vez, usado quando tenho certeza de que o erro não está nela e não quero
# investigar o seu funcionamento em detalhes.
