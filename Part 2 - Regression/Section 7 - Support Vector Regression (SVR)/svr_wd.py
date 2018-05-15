#SVR

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
#SVR doesn't use feature scaling because its a lesser used model, so the clases and libraries defined here do not take of feature scaling 
#when we feature scale the data, we get a warning that the StandardScalar() class we used, has converted the data from integer(orignally) to float, but its not to worry about 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
sc_y = StandardScaler()


# Fitting the SVR to the dataset
from sklearn.svm import SVR
#the most important parameter among all is the kernel paramater, which decides whether to fit a linear, polynomial or gaussain SVR
regressor= SVR(kernel='rbf')
regressor.fit(X,y)



# Predicting a new result
'''
1. Firstly, predict() requires a matrix in it. So we use numpy's array() function to convert it into a vector.Then we again need to convert in into a matrix by applying extra [] brackets.
2. We need to inverse_transform() the data because we dont want to get a scaled output.  
 '''
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()




#We can see that the SVR model is not fitting to this data right here at the top(CEO) because the CEO is considered as an outlier here. The SVR has some penalty parameters set by default in its algorithm and therefore the CEO point is quite far from all other points, and so the SVR cosnidered it as an outlier and fitted the model to other data points 