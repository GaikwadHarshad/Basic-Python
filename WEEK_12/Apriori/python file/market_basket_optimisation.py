#!/usr/bin/env python
# coding: utf-8

# In[23]:


# import libraries
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  


# In[24]:


# import dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)


# In[25]:


# size of dataset
print('Dataset has {} rows and {} columns'.format(dataset.shape[0],dataset.shape[1]))


# In[26]:


# display some data
dataset.head()


# In[27]:


# convert dataset into list of list for each transaction
transactions = []
for i in range(0,dataset.shape[0]):
    transactions.append([str(dataset.values[i,j]) for j in range(0,dataset.shape[1])])


# In[31]:


# training apriori on dataset
rules = apriori(transactions,min_support=0.003,min_confidence=0.2, min_lift=3, min_length=2)


# In[32]:


# view result in list format
rules = list(rules)


# In[33]:


for item in rules:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " ----> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("\n\n")


# In[ ]:




