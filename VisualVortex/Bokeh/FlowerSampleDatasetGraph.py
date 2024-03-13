# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 01:33:29 2020

@author: ADMIN
"""

#importing libraries
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.sampledata.iris import flowers

#print the samplpe dataset imported from bokeh sampledata
print(flowers)

#creating two dataframes with length and width og petals
petalLength=flowers['petal_length']
petalWidth=flowers['petal_width']


#creating figure's boject and storing the refrence in variable f
f=figure()

# creating the output_file
output_file('PetalsSampleGrapgh1.html')

f.triangle(petalLength, petalWidth)

show(f)