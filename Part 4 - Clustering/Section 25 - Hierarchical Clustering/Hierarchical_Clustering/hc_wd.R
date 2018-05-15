#Hierarchical Clustering

#Importing dataset

dataset= read.csv('Mall_Customers.csv')
X= dataset[4:5]

#Using the dendrogram to find optimal number of clusters
# dist: for each pair of customers, the eucledian distance b/w two
# ward.D minimizes within cluster variances
dendrogram = hclust(d = dist(dataset, method = 'euclidean'), method = 'ward.D')
plot(dendrogram,
     main = paste('Dendrogram'),
     xlab = 'Customers',
     ylab = 'Euclidean distances')

#Fitting hierarchical clustering to mall dataset
hc = hclust(d = dist(dataset, method = 'euclidean'), method = 'ward.D')
y_hc= cutree(hc,5)

#Visualising the clusters
library(cluster)
clusplot(dataset,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')