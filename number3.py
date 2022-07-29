try:
    x = int(input("Who's x? "))
except ValueError:
    print("x is not an integer")
print(f"x is {x}")
# Malan tenta cat nesta modificação e obtem um NameError. A partir do momento em que o segundo comando recebe um
# string, um ValueError ocorre, interrompendo a entrada desta variável em x. Por isso ela está indefinida e
# ocorre um NameError. O próprio PyCharm alerta para este problema.
