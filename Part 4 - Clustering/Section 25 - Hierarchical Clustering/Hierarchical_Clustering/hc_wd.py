#Hierarchical Clustering

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Importing mall dataset with pandas

dataset= pd.read_csv('Mall_Customers.csv')
X= dataset.iloc[:,[3,4]].values

#Using the dendogram to find optimum no of clusters
#In KMeans we minimized within cluster sum of squares, and here we are minimising within cluster variance i.e. variance within each cluster
import scipy.cluster.hierarchy as sch
dendrogram= sch.dendrogram(sch.linkage(X, method= 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Eucledian Distances')
plt.show()

#Fitting heirarchical clustering to mall dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)
#Visulasing the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

 