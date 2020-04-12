# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:00:42 2020

@author: ADMIN
"""
#importing bokeh libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

#reading cdv file using pandas read_csv method
BachelorsData=pd.read_csv("~//Downloads//bachelors.csv")

#Retriving the columns of pandas dataframe
print(BachelorsData.columns)
#print(BachelorsData)

#preparing dataset
Year=BachelorsData["Year"]
#print(Year)

EngineeringCount=BachelorsData["Engineering"]
#print(Engineering)


#creating figure object
f=figure()

#prepring the output file below commsnd will save the html file with specified name
output_file('BachelorsEngineering.html')



#Plotting the graph
f.line(Year,EngineeringCount)

#showing the graph
show(f)
