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

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']


while True:
    if starting_year == 2001:
        break
    try:
        day = calendar.weekday(starting_year,starting_month,starting_day)


        if (day == 6) and (starting_day == 1):
            count += 1


        starting_day += 1


        print(days[day])

    except ValueError:
        if starting_month != 12:

            starting_day = 1
            starting_month += 1
        else:
            starting_day = 1
            starting_month = 1
            starting_year += 1






print(count, "Sundays")