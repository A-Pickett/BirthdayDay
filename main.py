import calendar

calendar.setfirstweekday(0)


def which_day_is_my_birthday(year):
    day = calendar.weekday(year, 6, 22)
    days_of_week = {0: "Monday",
                    1: "Tuesday",
                    2: "Wednesday",
                    3: "Thursday",
                    4: "Friday",
                    5: "Saturday",
                    6: "Sunday"
                    }
    print("In {} your Birthday falls on a {}".format(year, (days_of_week[day])))


while True:
    yeartocheck = (input("Please enter a year and I will tell you which"
                         " day of the week your Birthday falls on: "))

    which_day_is_my_birthday(int(yeartocheck))
    print("-" * 40)
