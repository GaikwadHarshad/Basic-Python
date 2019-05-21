#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as  sch
from sklearn.cluster import AgglomerativeClustering
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# load dataset
dataset = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_12/Hierarchical Clustering/Datasets/Mall_Customers.csv')


# In[3]:


dataset.head()


# In[4]:


print("Dataset has {} rows and {} Columns".format(dataset.shape[0],dataset.shape[1])) 


# In[5]:


dataset.sample()


# In[6]:


# checking information about dataset
dataset.info()


# In[7]:


dataset.describe().T


# In[8]:


# checking null values in dataset
dataset.isnull().sum()


# In[9]:


# check for minimum dataset
dataset.min()


# In[10]:


# getting input as X
X = dataset.iloc[:,[3,4]].values


# In[11]:


# find optimal # clusters using dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
# plotting dendrogram for identifying optimal clusters
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()


# In[12]:


# fitting hierarchical clustering
hc =  AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc =  hc.fit_predict(X)


# In[13]:


# vector of clusters
y_hc


# In[14]:


# visualizing clusters
plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=100, c='slateblue',label='careful')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=100,c='teal',label='standerd')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=100,c='darkorchid',label='Target')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=100,c='maroon',label='careless')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=100,c='forestgreen',label='sensible')

plt.title('Clusters of Clients')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()


# In[ ]:




