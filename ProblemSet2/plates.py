def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Começar com pelo menos duas letras; OK
    # Máximo de 6 caracteres e mínimo de 2; OK
    # Não pode haver números entre letras; OK
    # O primeiro número não pode ser 0; OK
    # Não pode ter vírgula, espaços ou qualquer marca de pontuação. OK
    for n in s:
        if n.isnumeric():
            np = s.find(n)  # Estou buscando a posição do primeiro número
            break
        else:
            np = 6
    for c in s[::-1]:
        if c.isalpha():
            cp = s.rfind(c)  # Estou buscando a posição da última letra
            break
        else:
            cp = -1
    tc = 0
    for t in s:  # Preciso de uma contagem geral para eliminar qualquer ocorrência de ponto, espaço e vírgula
        if t.isalpha():
            tc = tc + 1
        elif t.isnumeric():
            tc = tc + 1
    return cp < np and s[:2].isalpha() and 2 <= len(s) <= 6 and n != "0" and len(s) == tc


main()
