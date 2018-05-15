#Eclat

#Data Preprocessing
#header= false tells R that first line of our dataset doesn't contain titles of the column
#install.packages('arules')
library(arules)
datset= read.csv('Market_Basket_Optimisation.csv',header = FALSE)
dataset=read.transactions('Market_Basket_Optimisation.csv',sep=',',rm.duplicates = TRUE)
summary(dataset)

itemFrequencyPlot(dataset,topN=10)

#Training Eclat on dataset
#choice of min and max support and confidence
rules= eclat(data = dataset,parameter = list(support=0.004 , minlen=2))

#Visualising the results
inspect(sort(rules, by='support')[1:10])
