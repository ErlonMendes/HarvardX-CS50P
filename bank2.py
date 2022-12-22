balance = 0


def main():
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()
# UnboundLocalError: local variable 'balance' referenced before assignment. Balance foi referenciada fora das funções
# de depósito e saque e não pode ser alterada por elas.
