import validators
email = input("What's your email address? ").strip()

if validators.email(email) is True:
    print("Valid")
else:
    print("Invalid")
