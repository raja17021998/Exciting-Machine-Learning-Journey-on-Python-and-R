# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:38:42 2018

@author: Narender 2
"""

#Polynomial Regression

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


# Fitting Linear Regression to the dataset

from sklearn.linear_model import LinearRegression
'''
lin_reg = LinearRegression()
lin_reg.fit(X, y)'''

'''
#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg= LinearRegression()
lin_reg.fit(X,y)'''


#Fitting Regression Model to dataset
from sklearn.preprocessing import PolynomialFeatures
#now we will change our matrix of features X to include certain non linear features which would be powers of that independent variable orignally.

#With the first three lines, we are tranformimg out matrix of features X to include polynomial features
#In the next two lines of code, we fitted our object lin_reg to our newly created X_poly and y(orignal) 
poly_reg= PolynomialFeatures(degree=4)
X_poly= poly_reg.fit_transform(X)
lin_reg2= LinearRegression()
lin_reg2.fit(X_poly, y)



#Visulising linear regressor

plt.scatter(X,y, color="red")
plt.plot(X, lin_reg.predict(X),color="blue")
plt.title("Truth vs Bluff Linear Regression..!!")
plt.xlabel("Position Table")
plt.ylabel("Salary")
plt.show()



#Visulising polynomial regressor

plt.scatter(X,y, color="red")
#we have directly not used X_poly here, because that would harcode our code. So we've let it open for entirely new set of martix X(new) which could be imported from entirely new datasets 
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)),color="blue")
plt.title("Truth vs Bluff Pplynomial Regression..!!")
plt.xlabel("Position Table")
plt.ylabel("Salary")
plt.show()

#Predicting a new result with Linear Regression
lin_reg.predict(6.5)

#Predicting a new result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))


