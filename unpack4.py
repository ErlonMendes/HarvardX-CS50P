def total(galleons, sickles, knuts):
    return (galleons*17 + sickles)*29 + knuts


coins = [100, 50, 25]
print(total(*coins), "Knuts")  # O * "desempacota" (unpack) os valores da lista e permite que coins seja colocado
# apenas uma vez.
