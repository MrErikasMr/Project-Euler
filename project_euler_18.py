import calendar



#1 Jan was a monday

# months with 31 days: Jan, Mar,May, July, August, October, December
# months with 30 days: April, June, September, November
# months that are odd: February
# leap years are when % 4 == 0, but not when the last two digits of a year are both 00 (divisbile by 100), unless it is % 400 == 0





starting_year = 1901
starting_month = 1
starting_day = 1


ending_year = 2000
ending_month = 12
ending_day = 31


count = 0


while True:
    if starting_year == 2001:
        break
    try:


        if (calendar.weekday(starting_year,starting_month,starting_day)  == 6) and (starting_day == 1):
            count += 1

        print(calendar.weekday(starting_year,starting_month,starting_day))
        starting_day += 1
        print(starting_year, "yoo")

    except ValueError:
        starting_day = 1
        starting_month += 1
        if starting_month >= 12:
            starting_day = 1
            starting_month = 1
            starting_year += 1



print(count, "Sundays")