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
import gc
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


# checking information about dataset
dataset.info()


# In[5]:


# get input data as X
X = dataset.iloc[:10000,:].values


# In[6]:


# find optimal # clusters using dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
# plotting dendrogram for identifying optimal clusters
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()


# In[7]:


# fitting hierarchical clustering
hc =  AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
y_hc =  hc.fit_predict(X)


# In[ ]:





# In[ ]:




