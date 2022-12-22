def main():
    fraction = input("Fraction: ")
    fraction_conv = convert(fraction)
    print(gauge(fraction_conv))


def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            percentage = int(fraction[0]) / int(fraction[1])*100
            if percentage <= 100:
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
