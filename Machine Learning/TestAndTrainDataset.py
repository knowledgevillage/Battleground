# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:47:34 2020

@author: ADMIN
"""

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#readgin the source dataset
raw_dataset=pd.read_csv("~//Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//Data.csv")

X=raw_dataset.iloc[:,:-1]
print(X)
Y=raw_dataset.iloc[:,3]
print(Y)


#to handel the NaN values in our dataset we will make use imputer from sklearn module
imputer_X= Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer_X=imputer_X.fit(X[:,1:3])

#X[:,1:3]=imputer_X.transform(X[:,1:3])
#print(X)