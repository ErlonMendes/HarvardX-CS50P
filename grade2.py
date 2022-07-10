score = int(input("Score [0..100]: "))
if 90 <= score <= 100:  # Mais uma que o Guanabara não ensinou
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
