def main():
    x = fuel_gauge("Fraction: ")
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{x:.0f}%")


def fuel_gauge(frac):
    while True:
        try:
            gauge = input(frac).split("/")
            perc = int(gauge[0]) / int(gauge[1]) * 100
            if perc <= 100:
                return perc
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass


main()
