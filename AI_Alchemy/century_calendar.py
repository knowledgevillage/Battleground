# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:23:48 2020

@author: ADMIN
"""

#python program to print of 100 years calendar
import calendar as cl

for yy in range(2000,2001):
    #print(cl.calendar(yy) )
    year_cal=cl.calendar(yy)
    for i in year_cal:
        print(i.values())
    

    