# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:09:54 2020

@author: ADMIN
"""

import datetime
# I started by creating lists for the months, their days, and the days of the week.
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def calendar(month, year):
    '''
    (int, int) -> None

    Prints a calendar for
    given month and year.

    CALLS: is_leap(year)

    CALLED BY: main()
    '''
    # I first wanted to check if the year is a leap year, and if so, modify the days in feb
    if is_leap(year):
        days_in_month[1] = 29
    # Now i set variables to values within my lists based of input data for year and month
    month_corrected = month_list[month-1]
    num_days = days_in_month[month-1]
    # Now I figure out what my start date is for the given month of the year
    day_one = datetime.date(year, month, 1)
    start_day = day_one.isoweekday()
    # Begin by printing the month and year
    print(month_corrected[:3], year)
    # Print the days of the week for my calendar
    print(' '.join(['{0:<2}'.format(w) for w in days_of_week]))
    # Print a blank space on the days before my start day variable
    print('{0:>3}'.format('')*start_day, end='')
    # if my start day begins on sunday, start a new line and set my start day to zero
    if start_day >= 7:
        print()
        start_day = 0
    # Begin looping through the number of days in the month starting with my start day
    for day in range(1, num_days+1):
        # Print each day
        print('{0:>2}'.format(day), end=' ')
        # up my start day variable each time to act as a counter
        start_day += 1
        if start_day >= 7:
            # If my start day variable is on Sunday, start new line
            print()
            # Reset my day counter
            start_day = 0
    print()

def is_leap(year):
    '''
    (int) -> bool

    Checks if year is a leap year
    credit to Steven Summers

    CALLS:

    CALLED BY: calendar()

    >>> is_leap(2000)
    True
    >>> is_leap(1900)
    False
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    '''
    () -> None

    Drives calendar program

    CALLS: calendar(month, year)

    CALLED BY:
    '''
    make_calendars = True
    while make_calendars:
        # create input loops for year and month to run calendar function
        good_year = False
        while good_year == False:
            input_year = input('Enter year (blank to exit): ')
            # some code to ensure input is within datetime parameters
            if input_year == '':
                make_calendars = False
                return None
            else:
                year = int(input_year)
                if 1 > year > 9999:
                    print("Must enter an integer between 1 and 9999")
                else:
                    good_year = True        
        good_month = False
        while good_month == False:
            # a blank entry will print the entire year
            input_month = input('Enter month (blank to print entire year: ')
            # some code to ensure input is within datetime parameters
            if input_month == '':
                for i in range(1,13):
                    calendar(i, year)
                main()
            else:
                if input_month[0] == '0':
                    input_month = input_month[1:]                
                month = int(input_month)
                if 1 > month > 12:
                    print("Must enter an integer between 1 and 12")
                else:
                    good_month = True 
        if good_year == True and good_month == True:
            calendar(month, year)

if __name__ == '__main__':
    main()