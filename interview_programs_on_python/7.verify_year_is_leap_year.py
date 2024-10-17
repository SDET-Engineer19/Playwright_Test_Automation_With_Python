import calendar


# 1st approach using calendar functions

def verify_entered_is_leap_year(year):
    flag = calendar.isleap(year)
    if flag:
        print(year, "is a Leap Year ")
    else:
        print(year, "is Not a Leap Year ")


#  2nd approach with conditions
def verify_entered_year_is_leap_or_not(year):
    # divide by 100 is century year (ending 00) , century year should divide by 400 is leap year
    # when it is not 100 means not century year, but it should divide by 4 to get leap year
    if year % 100 == 0 and year % 400 == 0:
        print("{0} is a leap year".format(year))
    elif year % 4 == 0 and year % 100 != 0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))




class leap_year:
    year = int(input("Enter Correct Year : "))
    # verify_entered_is_leap_year(year)
    verify_entered_year_is_leap_or_not(year)

