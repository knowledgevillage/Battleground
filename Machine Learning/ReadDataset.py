# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:45:00 2020

@author: ADMIN
"""

import pandas as pd
import os

print(os.getcwd())

dataset=pd.read_csv("~//Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//Data.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values='NaN', strategy='mean', axis=0 )
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(type(X))
print(X)


print(Y)
print(type(Y))

