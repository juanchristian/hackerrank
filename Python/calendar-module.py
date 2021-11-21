import datetime


def do_stuff(date: str):
    parts = date.split()
    dt = datetime.datetime(int(parts[2]), int(parts[0]), int(parts[1]))
    weekday = dt.weekday()
    if weekday == 0:
        print("MONDAY")
    elif weekday == 1:
        print("TUESDAY")
    elif weekday == 2:
        print("WEDNESDAY")
    elif weekday == 3:
        print("THURSDAY")
    elif weekday == 4:
        print("FRIDAY")
    elif weekday == 5:
        print("SATURDAY")
    elif weekday == 6:
        print("SUNDAY")


if __name__ == "__main__":
    dt = input()
    do_stuff(dt)
