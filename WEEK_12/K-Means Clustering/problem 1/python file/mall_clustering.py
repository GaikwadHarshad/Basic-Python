#!/usr/bin/env python
# coding: utf-8

# In[16]:


# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


# In[17]:


# load dataset
dataset = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_12/K-Means Clustering/Datasets/Mall_Customers.csv')


# In[18]:


dataset.head()


# In[19]:


print("Dataset has {} rows and {} Columns".format(dataset.shape[0],dataset.shape[1])) 


# In[20]:


dataset.sample()


# In[21]:


# checking information about dataset
dataset.info()


# In[22]:


dataset.describe().T


# In[23]:


# checking null values in dataset
dataset.isnull().sum()


# In[24]:


# check for minimum dataset
dataset.min()


# In[25]:


# get input data as X
X = dataset.iloc[:,[3,4]].values


# In[26]:


# Find optimal number of clusters using  elbow method

WCSS = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    WCSS.append(kmeans.inertia_)

# plot elbow graph
plt.plot(range(1,11),WCSS)
plt.title('The Elbow  Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# In[27]:


# Applying KMeans to mall_customer dataset
kmeans = KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
# find for each observation which cluster it belongs
y_kmeans = kmeans.fit_predict(X)


# In[29]:


# cluster 0-4 mean 1-5 clusters
y_kmeans


# In[32]:


# visualizing clusters
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=100, c='slateblue',label='careful')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=100,c='teal',label='standerd')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=100,c='darkorchid',label='Target')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=100,c='maroon',label='careless')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=100,c='forestgreen',label='sensible')

# plotting centroids
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300, c='yellow',label='Centroids')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()


# In[ ]:




