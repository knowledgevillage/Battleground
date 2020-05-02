# -*- coding: utf-8 -*-
#Created on Sun Apr 26 11:00:27 2020

#@author: ADMIN

#we are goint to make use of matplotlib to plot the graphf in python
from matplotlib import pyplot as plt

#we are going to use tow dataset set
#below is the age dataset, we will be using which represnts the average age group of certain people
age = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#below is the datase set of ave salesries for certain group of people
salary = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

# to plot the graph we will use plot mthod of plyplot libariry 
plt.plot(age,salary)


#xlabel and ylabel methods used to label the axis's
plt.xlabel('Ages')
plt.ylabel('Salaries')


# title method is used to give a tital to the plotted graph to make it more informative
plt.title('Median Salary (USD) by Age')

# to show the plotted grapsh we will use show methin of pyplot library
plt.show()