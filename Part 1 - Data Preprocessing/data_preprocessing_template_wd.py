# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:24:47 2018

@author: Narender 2
"""
#setwd("E:/Machine Learning Files/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing")

#Data preprocessing
 #importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset= pd.read_csv("Data.csv")
X= dataset.iloc[:, :-1].values
y= dataset.iloc[:,3].values






'''
#take care of missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean",axis=0)
imputer= imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
'''








'''
#encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X= LabelEncoder()
#line 31 will will use the fit_tranform() of LabelEncoder to encode our categorical variable country in our case 
X[:,0]=labelencoder_X.fit_transform(X[:,0])
#actually this [0] feature is categorical which is passed as a parameter of OneHotEncoder class' constructor 
onehotencoder= OneHotEncoder(categorical_features=[0])
#this line does the work for us. toarray() because we didn't want it to be only on the first column
X= onehotencoder.fit_transform(X).toarray()
#here we dont need to use the OneHotEncoder cause the ML variable will know that its a dependednt variable so it doesnt have any order of magnitude
labelencoder_y= LabelEncoder()
#remember X is a 2-D array where as y is a vector
y= labelencoder_y.fit_transform(y) 
'''



#splitting dataset into training set and test set
from sklearn.cross_validation import train_test_split
#X-train: Train set fror matrix of features X_test: testpart of matrix of features y_train: train part of dependent variable y_test:trstpart of dependent variable associated to matrix of features X
X_train, X_test, y_train,y_test= train_test_split(X, y, test_size= 0.3,random_state=0)












'''#feature scaling
from sklearn.preprocessing import StandardScaler 
sc_X= StandardScaler()
#You have to directly fit and transform() the training set. We are going to trasform X_train so we will recompute X_train because we want it to be scaled, so we take our object as sc_X and we are calling method fit_transform() 

 


X_train= sc_X.fit_transform(X_train)
#its important to understand when you are applying your object standard Schellar object to training set and you have to fit the object of training set and then transform it, you are going to see its not going to be the same thing for test set because we will only transform the test set, but for training set we need to transform it and then tranform to training set.

#In short(feature scaling will be applied on the training set not TEST SET..!!)
X_test= sc_X.transform(X_test)

#we need to ask 2 questions.!! 
#1. do we neeed to fit and transform the dummy variables
#we dont need to scale it as such. It doesn't make much of a difference...
'''







