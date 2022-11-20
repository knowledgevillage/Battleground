# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:54:55 2020

@author: ADMIN
"""

import pandas as pd
from sklearn.preprocessing import Imputer



covid_data=pd.read_csv("~/Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//covid19_by_country.csv")
pd.set_option('display.expand_frame_repr',False)
print(covid_data)

X=covid_data.iloc[:,:].values

print(X)

list_of_columns=list(covid_data.columns.values)
print(list_of_columns)


