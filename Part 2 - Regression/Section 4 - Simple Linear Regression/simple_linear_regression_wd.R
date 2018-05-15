#Simple Linear Regression

# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)






#Fitting simple linear regression to test set
#we use lm() which takes 2 arguments formula and data
#formula is the one by which we tell R that that we have a 
#linear relationship between b/w these variables. 
#and data is the one on which we operate
regressor= lm(formula= Salary ~ YearsExperience,
              data= training_set)
#Now summary(regressor) gives something important to us
#the 3 stars mean that the qty. is highly siginificant and 0 means its a waste 



#Predicting the test set results
y_pred= predict(regressor, newdata = test_set)
#our regressor will predict each of these observations for salary

#Visualising training set results
#only for newbies like us in R
#install.packages("ggplot2")





# Visualising the Training set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (Training set)') +
  xlab('Years of experience') +
  ylab('Salary')




# Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (Test set)') +
  xlab('Years of experience') +
  ylab('Salary')





 

              



