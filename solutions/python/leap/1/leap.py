""" Module define a function that check if a given year is a leap year."""
def leap_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) :
        return False
    return True
        