import requests
import sys


def main():
    n = get_number()
    rate = get_rate()
    print(f"${n * rate:,.4f}")


def get_number():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        try:
            n = float(sys.argv[1])
            return n
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)


def get_rate():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
        rate = response["bpi"]["USD"]["rate_float"]
        return rate
    except requests.RequestException:
        print("Request Exception")
        sys.exit(1)


if __name__ == "__main__":
    main()
