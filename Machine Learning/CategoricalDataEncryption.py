# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:57:15 2020

@author: ADMIN
"""

import pandas as pd
import os
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder as le
from sklearn.preprocessing import OneHotEncoder as ohe

#printing the current woring directory
print(os.getcwd())


#reading dataset

raw_dataset=pd.read_csv("~//Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//Data.csv")

#Deviding pandas dataset into two dataframes
X=raw_dataset.iloc[:,:-1].values

Y=raw_dataset.iloc[:,3].values

#replacing the not availble values with the mean value of that particual column
imputer_X=Imputer(missing_values="NaN", strategy="mean",axis=0)
imputer_X=imputer_X.fit(X[:,1:3])
X[:,1:3]=imputer_X.transform(X[:,1:3])


#categorial Data encoding

# Label encocder is the  is class It is used to endoce the lebel(i.e. non-numercial ctegories with values form 0 to n_classes-1)
#creating an obejct of label encoder
labelecoder_X= le()
X[:,0]=labelecoder_X.fit_transform(X[:,0])

#above code will conver the country codes into numercial values. It might can create confucion for user or differnnt algorithm which we will use to perform the analytics
#so to avoide that we will further encode these values using OneHotEncoder

#ONeHotEncoder is a class it encodes categorical integer features as one-hot numeric array. This encoding is needed for feeding categorical data to many scikit-learn estimators, notably linear models and SVMs with the standard kernels
"""The input to this transformer should be an array-like of integers or strings, denoting the values taken on by categorical (discrete) features.
This creates a binary column for each category and returns a sparse matrix or dense array."""

#By default, the encoder derives the categories based on the unique values in each feature. Alternatively, you can also specify the categories manually

# The OneHotEncoder previously assumed that the input features take on values in the range [0, max(values)). This behaviour is deprecated.


onehotencoder_X=ohe(categorical_features=[0])
X=onehotencoder_X.fit_transform(X).toarray()

#above code have create n columns for N categories.

#applying label encoder for Y object i.e. pruchsed indicatior
#crreating object of label encoder
labelencoder_Y=le()
Y=labelencoder_Y.fit_transform(Y)

