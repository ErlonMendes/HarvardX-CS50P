def main():
    time = input("What time is it? ").strip()
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    if time.rfind("a") == 5:
        time = time[0:5]
        hours, minutes = time.split(":")
        hours = int(hours)
    elif time.rfind("a") == 6:
        time = time[0:6]
        hours, minutes = time.split(":")
        hours = int(hours)
    elif time.rfind("p") == 5:
        time = time[0:5]
        hours, minutes = time.split(":")
        hours = int(hours) + 12
    elif time.rfind("p") == 6:
        time = time[0:6]
        hours, minutes = time.split(":")
        hours = int(hours) + 12
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
