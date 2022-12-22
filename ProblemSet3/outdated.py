months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if date.find("/") != -1:
            date = date.split("/")
            if int(date[0]) < 12 and int(date[1]) < 31:
                print(f"{int(date[2])}-{int(date[0]):02d}-{int(date[1]):02d}")
                break
            else:
                pass
        else:
            date = date.split(" ")
            if date[1].find(",") != -1:
                comma = "True"
            else:
                comma = "False"
            date[1] = date[1].replace(",", "")
            if int(date[1]) < 31 and comma == "True":
                print(f"{int(date[2])}-{months.index(date[0]) + 1:02d}-{int(date[1]):02d}")
                break
            else:
                pass
    except ValueError:
        pass
