# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:47:34 2020

@author: ADMIN
"""

#import pandas to read a csv file 
import pandas as pd
#import numpy to handel nan values imputer method
import numpy as np
#SimpleImputer is class to impute the missing values, imported from impute module of sklearn library
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
# we will import train_test_split function from model selection module to split the dataset into training and test dataset
from sklearn.model_selection import train_test_split


#readgin the source dataset
raw_dataset=pd.read_csv("~//Documents//DataScience//Machine_learning_a_to_z//Data_Preprocessing//Data.csv")

X=raw_dataset.iloc[:,:-1].values
print(X)
Y=raw_dataset.iloc[:,3].values
print(Y)


#to handel the NaN values in our dataset we will make use imputer from sklearn module
imputer_X= SimpleImputer(missing_values=np.nan, strategy="mean", verbose=0)
imputer_X=imputer_X.fit(X[:,1:3])
X[:,1:3]=imputer_X.transform(X[:,1:3])
print(X)

#creating the obejct of  ColumnTransformer. It is a calss and will be used to encode the data. using this class we will enable us to encode the data in lesser steps. It will take two arguments:
# 1. transformers : here we specify what kinf of transformation we wwant to do and on which columns. Here we want to do OneHot encoding so we will mention that
# 2. reinader : is used to specify whether we want to keep the rest of the columns. if we do not keep "remainder='passthrough'" then below code will give us just one column resulting hotencoding.
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
#transformers argument here we have to specify three things and these have to be specified into square brackets insde tuple 
# 1. kind of tranformation i.e. encoding 
# 2. kind of ancoding i.e. OneHotEncoding
# 3. colmn number we want to  encode i.e. country	

# now we do not have to use use two methods tranform and fit as ColumnTransformer have on fit_transform which does the work inside which we pass the dataset which we want to transform
X= np.array(ct.fit_transform(X))
# fit_tranform method of ColumnTransformer class will not retur a numpy array but it should have to be a num[ay array as further we will devide the dataset into train and test dataset. Hence we will use array method numpy library to convert the output to numpy array

print(X)

#now we will use the Label encoder to encode the Y dataset
labelEncoder_Y=LabelEncoder()
Y=labelEncoder_Y.fit_transform(Y)
print(Y)


#now we will devide the original datasets into training and test datasets
X_Train, X_Test, Y_Train,  Y_Test=train_test_split(X,Y,test_size=0.2, random_state=1)

print("************************* Print the traing datasets ****************************")

print(X_Train)

print(Y_Train)

print("************************* Print the  test datasets ****************************")

print(X_Test)

print(Y_Test)

