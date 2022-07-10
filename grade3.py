score = int(input("Score [0..100]: "))
if score >= 90:
    print("Grade: A")
elif score > 80:  # Como eu usei o elif, testar o limite superior desta pergunta é redundante
    print("Grade: B")
elif score > 70:
    print("Grade: C")
elif score > 60:
    print("Grade: D")
else:
    print("Grade: F")
