import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        ip_list = ip.split(".")
        for number in ip_list:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
