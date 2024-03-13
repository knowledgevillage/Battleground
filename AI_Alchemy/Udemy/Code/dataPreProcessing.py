# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:00:11 2022

@author: ADMIN
"""
import pandas as pd
import pathFinder as pf
import logging 
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
 
logging.basicConfig(level=logging.DEBUG)

logging.debug('finding the file location')

srcFilePath=pf.get('Data.csv')

srcFile=pd.read_csv(srcFilePath)

print(srcFile)

logging.debug(" let's do some analysis on top of source file info")

srcFile.info()

logging.debug("Lets see the summary of dataset by describe")

print(srcFile.describe())


logging.info("Lets devide datase into feature and dependent vairable")

X=srcFile.iloc[:,:-1].values
Y=srcFile.iloc[:,-1].values

logging.info("Data set has beend devided into feature category and deendent vairable")

logging.info('values of feature category')
print(X)

logging.info('values of dependent variable')
print(Y)

logging.info("Let's handel the null values as we have to ultimatly train the ML model and null needs to be handeled for that")


imputer=SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(X[:,1:3])
logging.debug("Lets tranform these null vallues with mean of that column")

X[:,1:3]=imputer.transform(X[:,1:3])

print(X)

logging.info("Let's encode categorilcal data")

ct=ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0])], remainder='passthrough'   )
X=np.array(ct.fit_transform(X))


print(X)

logging.info("Lets encode the dependent variable")
le=LabelEncoder()
Y=le.fit_transform(Y)

print(Y)



# Spliting Data set into Training and Test

logging.info("Spliting dataset into test and train data set")

from sklearn.model_selection import train_test_split

XTrain, XTest, YTrain, YTest = train_test_split(X,Y, test_size=0.2, random_state=1)

logging.info("Lets see the test and train set values")

print("Train Set \n")
print(XTrain)
print(YTrain)
print("Test Set \n")
print(XTest)
print(YTest)
