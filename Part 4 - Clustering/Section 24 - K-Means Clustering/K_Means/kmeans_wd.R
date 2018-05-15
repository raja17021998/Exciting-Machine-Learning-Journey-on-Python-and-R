#KMeans Clustering

#Importing the dataset

dataset = read.csv("Mall_Customers.csv")
X= dataset[4:5]

#using the elbow method to find optimal number of clusters

set.seed(6)
wcss <- vector()
#for loops in R include upper and lower bound
#at each iteration, we directly compute the within cluster sum of squares, for each number i of clusters by writing sum() function
#withins computes within cluster sum of squares
for (i in 1:10) wcss[i] = sum(kmeans(dataset, i)$withinss)
plot(1:10,
     wcss,
     type = 'b',
     main = paste('The Elbow Method'),
     xlab = 'Number of clusters',
     ylab = 'WCSS')
#Applying Kmeans to DATSET
set.seed(29)
kmeans= kmeans(X,5,iter.max = 300,nstart = 10)

#Visualising Clusters

library(cluster)
clusplot(X ,
         kmeans$cluster,
         lines=0,
         shade=TRUE,
         color =TRUE,
         labels=2,
         plotchar=FALSE,
         span = TRUE,
         main = paste('Cluster of Clients'),
         xlab = 'Annual Income',
         ylab='Spending Score')

