answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer.strip() == "42" or answer.lower().strip() == "forty-two" or answer.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
