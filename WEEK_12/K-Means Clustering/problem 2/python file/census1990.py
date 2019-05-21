#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# load dataset by chunksize of 100000 with cpu time
get_ipython().run_line_magic('time', 'data = pd.read_csv(\'/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_12/K-Means Clustering/Datasets/USCensus1990.data.txt\',delimiter=",", sep=\'\\t\', iterator=True, chunksize=10000)')
dataset =  pd.concat(data,ignore_index=True)
dataset.head()


# In[3]:


print("Dataset has {} rows and {} Columns".format(dataset.shape[0],dataset.shape[1])) 


# In[4]:


dataset.sample()


# In[5]:


# checking information about dataset
dataset.info()


# In[6]:


dataset.describe().T


# In[7]:


# checking null values in dataset
dataset.isnull().sum()


# In[8]:


# get input data as X
X = dataset.iloc[:20000,:].values


# In[9]:


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


# In[10]:


# Applying KMeans to mall_customer dataset
kmeans = KMeans(n_clusters=3,init='k-means++',max_iter=300,n_init=10,random_state=0)
# find for each observation which cluster it belongs
y_kmeans = kmeans.fit_predict(X)


# In[ ]:





# In[ ]:




