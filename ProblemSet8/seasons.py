from datetime import date
import re
import sys
import inflect
p = inflect.engine()


def main():
    birth = input("Date of Birth: ")
    d_today = date.today()
    t_year = d_today.year
    try:
        year, month, day = check_birthday(birth)
    except ValueError:
        sys.exit("Invalid date")
    d_birth = date(int(year), int(month), int(day))
    diff = d_today - d_birth
    minutes = diff.days*24*60
    output = p.number_to_words(minutes, andword="")
    print(output.capitalize() + " minutes")


def check_birthday(birth):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth):
        year = matches.group(1)
        month = matches.group(2)
        day = matches.group(3)
        if int(year) > 2022 or int(month) > 12 or int(day) > 31:
            raise ValueError
        else:
            return year, month, day
    else:
        raise ValueError


if __name__ == "__main__":
    main()
