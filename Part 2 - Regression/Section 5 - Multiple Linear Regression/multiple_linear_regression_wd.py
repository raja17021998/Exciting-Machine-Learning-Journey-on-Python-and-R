# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Encoding categorical data
#Encoding the independent variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X= LabelEncoder()
X[:, 3]= labelencoder_X.fit_transform(X[:, 3])
onehotencoder= OneHotEncoder(categorical_features=[3])
X= onehotencoder.fit_transform(X).toarray()

#Avoiding dummy variable trap
X= X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


#Fitting multiple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train, y_train)


#Predicting the test set results
y_pred= regressor.predict(X_test)

#Simple graph
# Visualising the Test set results
#plt.scatter(y_test, y_pred, color = 'red')
plt.plot(y_test, y_pred, color = 'blue')
plt.xlabel('Test')
plt.ylabel('Predicted')
plt.show()

#Building optimal model using BackwardElimination
#Statistical siginificance for data
#Basic goal is to find a team of independent set of variables that have startegically greater impact on our predictions
import statsmodels.formula.api as sm
#we need to add a column of ones to our matrix of features. Recall the eqn.of multivariate linear regression, y= b(0)+b(1)x(1)+b(2)x(2)+b(3)x(3)+......+b(m)x(m), the constant b(0). Its for that x(0)=1. The LinearRegression class takes into account the constant thing, but its not the case with statsmodels library
X= np.append(np.ones((50,1)).astype(int), values=X, axis=1)
#X_opt will only contain those independent features which will have greater impact on the final output
X_opt =X[:,[0,1,2,3,4,5]]
#we need to crate object of OLS class. Arguments passed are endog(dependednt variable) and exog(independent variable) and we need to fit this regressor_OLS  object using fit() function
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#we eliminate one by one
X_opt =X[:,[0,1,3,4,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


X_opt =X[:,[0,3,4,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt =X[:,[0,3,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt =X[:,[0,3]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()























































































































































































