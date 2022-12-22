import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-2]?\d):?(\d{2})? (AM|PM) to ([1-2]?\d):?(\d{2})? (AM|PM)$", s):
        if (int(matches.group(1)) <= 12 and int(matches.group(4)) <= 12) \
                and (matches.group(2) is None or int(matches.group(2)) < 60) \
                and (matches.group(5) is None or int(matches.group(5)) < 60):
            if matches.group(3) == "PM":
                if int(matches.group(1)) == 12:
                    hour1 = 12
                else:
                    hour1 = int(matches.group(1)) + 12
            else:
                if int(matches.group(1)) == 12:
                    hour1 = 0
                else:
                    hour1 = int(matches.group(1))
            if matches.group(2) is None:
                minute1 = 0
            else:
                minute1 = int(matches.group(2))
            if matches.group(6) == "PM":
                if int(matches.group(4)) == 12:
                    hour2 = 12
                else:
                    hour2 = int(matches.group(4)) + 12
            else:
                if int(matches.group(4)) == 12:
                    hour2 = 0
                else:
                    hour2 = int(matches.group(4))
            if matches.group(5) is None:
                minute2 = 0
            else:
                minute2 = int(matches.group(5))
            return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
