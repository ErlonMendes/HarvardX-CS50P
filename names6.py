with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line)
# Haverá linhas em branco entre as frases
