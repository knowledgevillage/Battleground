# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:51:53 2020

@author: ADMIN
"""

import numpy as np
import pandas as pd
"""Scikit-learn is a free machine learning library for Python. It features various algorithms like support vector machine, random forests, and k-neighbours, 
and it also supports Python numerical and scientific libraries like NumPy and SciPy"""

#importing the SimpleImputer class from  impute module of sklearn library
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

#read csv file to create pandas dataset
raw_dataset=pd.read_csv('~//Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//Data.csv')

#now devide tha dataset into two parts
X=raw_dataset.iloc[:,0:3].values

Y=raw_dataset.iloc[:,3].values

# now we have to impute the missing values. we will make use of SimpleImpputer
"""create Simputer object with appropriate aruments
1. missing values here it is np.nan which indicates that are tha NaN values in ouor dataset. Which are identified by using numpy library
2. strategy here we define the moethodolgy, hoe to replace missing numbers. we have multiple methodologies to replace a missing number such as 
    a.mean
    b.median
    c.most_frequent
    d.constant etc.
3. verbose it is an optional argument. As Matthew states it is generally an option for producing detailed logging information. You should be aware,
 and will probably notice if you enable verbose > 0, that printing to the screen is generally a very slow process. The algorithm may run an order of magnitude slower,
 or more, with verbose enabled. Also, in multi-threaded applications, input/output operations are often disabled. Thus as the documentation advises, 
 writing to the standard output may not work in a multi-threaded context.
"""
imputer_X=SimpleImputer(np.nan, strategy='mean', verbose=0)
"""now we will use the fit method. it will filt the imputer (i.e. object with applied strategy) on dataset with misssinf values. It will retun SimpleImputer object. 
Or simpe to say The fit() function calculates the values of these parameters"""
#imputer_X=imputer_X.fit(X[:,1:3])
#print(imputer_X)
""" now we will use tranform method, and is used to impute (i.e. to represnt the imputer objects resultant values) all the missing values 
The transform function applies the values of the parameters on the actual data and gives the normalized value. """
#X[:,1:3]=imputer_X.transform(X[:,1:3])
#print(X)

# we can make use of fit_tranform method of insetd of doing it in two steps we can do above tranformation in one step. fit_transform means to do some calculation and then do transformation (say calculating the means of columns from some data and then replacing the missing values).
"""The fit() function calculates the values of these parameters.
 The transform function applies the values of the parameters on the actual data and gives the normalized value.
 The fit_transform() function performs both in the same step. Note that the same value is got whether we perform in 2 steps or in a single step."""
X[:,1:3]=imputer_X.fit_transform(X[:,1:3])
print(X)


#create column tranformer object to perform the encoding
ct=ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(X)
print(X)

# perform the label encoding on another set of data here too we are going to make use of fit_transform method insted of using fit and transform method sepratly. 

lbe_Y=LabelEncoder()
Y=lbe_Y.fit_transform(Y)
print(Y)

#make use of train_test_split function to categories the data accordingly
train_X, test_X, train_Y, test_Y=train_test_split(X,Y, test_size=0.2, random_state=1)

print("************************* Print the traing datasets ****************************")

print(train_X)

print(train_Y)

print("************************* Print the  test datasets ****************************")

print(test_X)

print(test_Y)
