year = int(input("Enter the year: "))

def is_leap(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            print(year, "is a leap year")
    else:
            print(year, "is not a leap year")

is_leap(year)