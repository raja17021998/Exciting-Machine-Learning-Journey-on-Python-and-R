#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset with pandas

dataset = pd.read_csv('Mall_Customers.csv')
X= dataset.iloc[:,[3,4]].values



#using the elbow method to find exact number of clusters

from sklearn.cluster import KMeans
#so as to plot the graph, we are going to compute wing cluster sum of squares for 10 different numbers.So we are going to write a for loop to write 10 different cluster sum of squares for the 10 number of clusters
wcss=[]
for i in range(1,11):
    #in each iteraion we are doing 2 things:
    #fit the KMeans to dataset
    #compute the within clusrers sum of squares and append to wcss list
    #max_iter: maximum no of iterations that can be defined to final clusters, when k-means algo is running.
    #n_init: max no of centroids our Kmeans will run
    kmeans= KMeans(n_clusters=i, init="k-means++", max_iter=300, n_init=10,random_state=0)
    kmeans.fit(X)
    #WCSS: Within Clusters Sum of Squares
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title("Elbow Show Method")
plt.xlabel("No of Clusters")
plt.ylabel("WCSS: Inertia")
plt.show()



#Applying KMeans to Mall Dataset
kmeans= KMeans(n_clusters=5, init="k-means++", max_iter=300, n_init=10,random_state=0)
#instead of fit() we use fit_predict() which returns to which cluster the these points belong to. It will return cluster number into a vector which we call y_kmeans
y_kmeans= kmeans.fit_predict(X)

#Visualising The Clusters

plt.scatter(X[y_kmeans==0,0], X[y_kmeans==0,1],s=100, c='red',label="Careful")
plt.scatter(X[y_kmeans==1,0], X[y_kmeans==1,1],s=100, c='green',label="Standard")
plt.scatter(X[y_kmeans==2,0], X[y_kmeans==2,1],s=100, c='blue',label="Target")
plt.scatter(X[y_kmeans==3,0], X[y_kmeans==3,1],s=100, c='yellow',label="Careless")
plt.scatter(X[y_kmeans==4,0], X[y_kmeans==4,1],s=100, c='orange',label="Sensible")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='magenta', label="Cluster Centroids")
plt.title("Cluster of Clients")
plt.xlabel("Annual Income in Dollars")
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()
  

    


