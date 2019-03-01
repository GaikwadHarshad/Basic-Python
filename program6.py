"""  Write a Python program to calculate number of days between two dates.
    Sample dates : (2014, 7, 2), (2014, 7, 11)
    Expected output : 9 days. """

from datetime import date
date1 = date(2019, 2, 14)
date2 = date(2019, 2, 26)
calculatedDays = date2 - date1
delta = calculatedDays
print("Total numbers of days between two dates :", delta.days, "days")
