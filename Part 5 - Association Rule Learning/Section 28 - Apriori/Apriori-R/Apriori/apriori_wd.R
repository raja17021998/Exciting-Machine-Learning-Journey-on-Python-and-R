#Apriori Algorithm

#Data Preprocessing
#header= false tells R that first line of our dataset doesn't contain titles of the column
#install.packages('arules')
library(arules)
datset= read.csv('Market_Basket_Optimisation.csv',header = FALSE)
dataset=read.transactions('Market_Basket_Optimisation.csv',sep=',',rm.duplicates = TRUE)
summary(dataset)

itemFrequencyPlot(dataset,topN=10)

#Training Apriori on dataset
#choice of min and max support and confidence
rules= apriori(data = dataset,parameter = list(support=0.004 , confidence=0.2))

#Visualising the results
inspect(sort(rules, by='lift')[1:10])