"""it just returns True if leap year bro"""
def leap_year(year):
    """
        returns True if leap year else False

        params:
            year: (int) the year duh

        returns:
            bool: yes leap? True!! else nuuh False!!

        2100 is divisible by 4, divisible by 100 but not divisible by 400 so it is not a leap yer
        if a year is divisible by 100 it must be divisible by 400 to be a leap year
        or to say it simply

        a year is a leap year if it is divisible by 4 and it is not divisible by 100 or it is divisible by 400
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
