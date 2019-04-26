#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt


# In[2]:


# load dataset
df=pd.read_csv("bankKNN.csv",delimiter=';')
df.head()


# In[3]:


# display columns in dataset
df.columns


# In[4]:


df.dtypes


# In[5]:


# display shape of dataset
print('dataset has {0} rows and {1} column'.format(df.shape[0],df.shape[1]))


# In[6]:


df.describe()


# In[7]:


# checking missing values
df.columns[df.isnull().any()]


# In[8]:


target = df.skew()
sb.distplot(target)


# In[9]:


df.isnull().values.any()


# In[10]:


# replace value -1,1 for <=50K/>50K
df['y'].replace('yes',1,inplace=True)
df['y'].replace('no',0,inplace=True)


# In[11]:


df['y'].value_counts()


# In[12]:


sb.countplot(x='y',  data=df, palette='hls')
plt.show()


# In[13]:


df.duplicated().sum()


# In[14]:


df.shape


# In[15]:


# convert  categorical data into binary data
df = pd.get_dummies(df)
df.head()


# In[16]:


df.shape


# In[17]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[18]:


df = Feature_Scaling(df)


# In[19]:


# split data into train and test
def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[20]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)


# In[21]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.y
    return df.drop('y', axis=1), output


# In[22]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[23]:


import random
import math
import operator


class KNN_Algorithm:
    def __init__(self):
        self.k = 3
        
#     calculate distance between two data instances using euclidean distance
    def euclidean(self,test,train,test_lenth):
        distance = 0
#         iterate lenth of times of test data
        for l in range(test_lenth):
            distance += pow(test[l]-train[l],2)
        return math.sqrt(distance)
        
#         get neighbors having least distance from new point
    def find_neighbours(self,x_train_data,y_train_data,x_test_data, k):
        distances = []
        test_lenth = len(x_test_data)-1
#         iterate over x_train_data
        for i in range(len(x_train_data)):
#         getting least distance between test data and train data[ith data]
            dist = self.euclidean(x_test_data,x_train_data[i],test_lenth)
#     adding distances into list
            distances.append((y_train_data[i],dist))
#         sort the list in ascending order
        distances.sort(key=operator.itemgetter(1))
        neighbors =  []
        
#         getting k most similar neighbors 
        for k in range(k):
            neighbors.append(distances[k][0])
        return neighbors
        
         
#       get response and decide which class it belongs 
    def getResponse(self,neighbors):
        classVotes = {}
#         iterate over lenth of neighbors
        for x in range(len(neighbors)):
#         get each neighbors response
            response = neighbors[x]
            
#         get response belongs to which class and add it in that class 
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
                
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
    
#     calculate accuracy
    def getAccuracy(self,x_test_data, predictions):
        correct = 0
        for x in range(len(x_test_data)):
            if x_test_data[x] == predictions[x]:
                correct += 1
        return (correct/float(len(x_test_data))) * 100.0
        
        
def main():
    obj = KNN_Algorithm()
    # calling method by class object
    x_train_data = np.array(train_data_x[:2000])
#     print("x_train_data:",x_train_data.shape)
    y_train_data = np.array(train_data_y[:2000])
     
    x_test_data = np.array(test_data_x[:200])
#     print("x_test_data:",x_test_data.shape)
    y_test_data = np.array(test_data_y[:200])
    
#     generate predictions
    predictions=[]
    k = 3
#     iterate over x_test_data 
    for x in range(len(x_test_data)):
#         finding neighbors from train data for given test data
        neighbors = obj.find_neighbours(x_train_data,y_train_data,x_test_data[x], k)
#     get responses of neighbors
        result = obj.getResponse(neighbors)
        predictions.append(result)
#         print('> predicted=' + repr(result) + ', actual=' + repr(x_test_data[x][-1]))
#    get accuracy over predicted data and test data
    accuracy_test = obj.getAccuracy(y_test_data, predictions)

    print('Test Accuracy: ' + repr(accuracy_test) + '%')
main()


# In[ ]:




