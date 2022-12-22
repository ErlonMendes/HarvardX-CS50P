def main():
    balance = 0  # Balance agora é uma variável local, continua fora das funções de depósito e saque e não pode ser
    # alterada por elas.
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()
