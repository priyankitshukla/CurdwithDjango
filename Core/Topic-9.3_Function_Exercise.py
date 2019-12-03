# Write a program using function to calculating employee Exp, Take input as joining year and substract from current year.

import datetime


def calculate_exp(year):
    now = datetime.datetime.now()
    return now.year - int(year)


joining_year = input('Please enter your joining year to HCL : ')
print(f" Your are in HCL by {calculate_exp(joining_year)} years.")
