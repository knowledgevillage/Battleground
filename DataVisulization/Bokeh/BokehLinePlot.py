# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:51:01 2020

@author: ADMIN
"""
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import show, output_file


#prepare some data
x=[10,56,567,38]
y=[5,6,9,7]

#prepare the output file
output_file('LineGrapgh.html')

#creating figure object 
f=figure()

# creating a line plot
f.line(y,x)

show(f)
