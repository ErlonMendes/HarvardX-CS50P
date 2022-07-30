def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":  # Resolve o problema da execução obrigatória do main, para usar este programa como biblioteca
    main()
