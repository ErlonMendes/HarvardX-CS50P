def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


if (
    __name__ == "__main__"
):  # Só executa o main caso o próprio programa seja executado. Resolve o problema da execução
    # obrigatória do main, permitindo usar este programa como biblioteca pessoal das suas funções
    main()
