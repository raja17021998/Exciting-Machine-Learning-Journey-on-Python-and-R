#Multiple Linear Regression
#
#Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50_Startups.csv')
# Encoding categorical data
dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)




#Fitting Multiple Linear Regression to out training set
regressor= lm(formula = Profit ~ R.D.Spend,
              data=training_set)
#lower the p-value is, higher the siginificant value it is for our prediction
#threshold= 5% (we have set this)

#Predicting test set results
y_pred= predict(regressor, newdata= test_set)

#Building optimal model using Backward Elimnation
summary(regressor)
#keep on seeing the summary(regressor) and remove variables on the basis of p-value





