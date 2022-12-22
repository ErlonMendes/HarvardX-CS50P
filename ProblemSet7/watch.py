import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^.*(?:http://youtube.com/|https://youtube.com/|https://www.youtube.com/)embed/(\w+)\".*$", s):
        video = matches.group(1)
        return f"https://youtu.be/{video}"


if __name__ == "__main__":
    main()
