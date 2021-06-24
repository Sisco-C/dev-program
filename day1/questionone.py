def check_for_leap_year(year) :
    if year % 4 == 0 and year % 400 == 0:
        print(bool(year))
    elif year % 100 == 0:
        print(bool())
year = input("Input Gregorian Year: ")
check_for_leap_year(int(year))




