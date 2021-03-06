#Data preprocessing
  setwd("E:/Machine Learning Files/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Preprocessing")

#importing dataset
  dataset= read.csv("Data.csv")

#taking care of missing data

# dataset$Age=ifelse(is.na(dataset$Age),
#                    ave(dataset$Age, FUN=function(X) mean(X,na.rm=TRUE)),
#                    dataset$Age)
# dataset$Salary=ifelse(is.na(dataset$Salary),
#                       ave(dataset$Salary, FUN=function(X) mean(X,na.rm=TRUE)),
#                       dataset$Salary)

#encoding categorical data

# dataset$Country = factor(dataset$Country,
#                          levels = c('France','Germany','Spain'),
#                          labels = c(1,2,3))









#Splitting dataset into tarining and test sets
  #install.packages('caTools')
  library(caTools)
  #to seed a random generator to get our and sir's results to be the same
  set.seed(123)
#The below function will split the data, and what sample.split() will return is a
#is a true false value for every entry in our dataset that has been partioned into
#train set i.e. true if it goes to training set

  split= sample.split(dataset$Purchased, SplitRatio = 0.8)
  training_set= subset(dataset,split==TRUE)
  test_set= subset(dataset,split==FALSE)






#feature scaling
# training_set[,2:3]= scale(training_set[,2:3])
# test_set[, 2:3]= scale(test_set[,2:3])















