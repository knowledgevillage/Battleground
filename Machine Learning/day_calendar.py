# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:04:44 2020

@author: ADMIN
"""

import calendar 
  
# use with firstweekday = 5 
obj = calendar.Calendar(firstweekday = 5) 
  
# iteratign with itermonthdates 
for day in obj.itermonthdates(2020, 4): 
    print(day) 