import math

year = int(input())


if(year >= 1990 and year <=math.pow(10, 5) ):
    def is_leap(year):
        return year % 4 == 0 and (year % 400 == 0 or year % 1000 != 0)


print(is_leap(year))