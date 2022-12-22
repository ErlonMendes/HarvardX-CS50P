def total(galleons, sickles, knuts):
    return (galleons*17 + sickles)*29 + knuts


coins = {"knuts": 25, "galleons": 100, "sickles": 50}
print(total(**coins), "Knuts")  # ** desempacota valores de um dicionário, com a vantagem de passar tanto as chaves
# quanto os valores. Mesmo que a ordem seja alterada no dicionário, vai funcionar.
