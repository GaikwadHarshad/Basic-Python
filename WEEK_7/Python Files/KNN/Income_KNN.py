#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt


# In[4]:


# load dataset
df=pd.read_csv("classification_2.csv",delimiter=',')
df.head()


# In[5]:


# rename columns
df.columns=[
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial_Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital_Gain", "Capital_Loss",
        "Hours_per_week", "Country", "Target"]


# In[6]:


df.head()


# In[7]:


df['Education'].unique()


# In[8]:


df['Target'].unique()


# In[9]:


# df.isnull().sum()


# In[10]:


df.isnull().values.any()


# In[11]:


# replace value -1,1 for <=50K/>50K
df['Target'].replace(' <=50K',-1,inplace=True)
df['Target'].replace(' >50K',1,inplace=True)


# In[12]:


df.head()


# In[13]:


# display columns in dataset
df.columns


# In[14]:


df.dtypes


# In[15]:


# display shape of dataset
print('dataset has {0} rows and {1} column'.format(df.shape[0],df.shape[1]))


# In[16]:


df.info()


# In[17]:


# checking missing values
df.columns[df.isnull().any()]


# In[18]:


# getting target value greater  than 50k and less than 50k
df['Target'].value_counts()


# In[19]:


# plot Target of <=50k and >50k
sb.countplot(x='Education',  data=df, palette='hls')
plt.show()


# In[20]:


sb.countplot(x='Target',  data=df, palette='hls')
plt.show()


# In[21]:


df.duplicated().sum()


# In[22]:


# remove duplicated values from dataframe
df.drop_duplicates(keep=False, inplace=True)
df.duplicated().sum()


# In[23]:


df.shape


# In[24]:


# correlation of multivariate variable
# temp=df.corr(method='pearson')
# temp.head(11)
# corr['Target'].sort_values(ascending=False)[:]


# In[25]:


corr = df.corr()
sb.heatmap(corr)


# In[26]:


df.shape


# In[27]:


df.dtypes


# In[28]:


df = pd.get_dummies(df,columns=["Workclass","Education","Martial_Status","Occupation","Relationship", "Race", "Sex","Country"])
df.head()


# In[29]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[30]:


df = Feature_Scaling(df)


# In[31]:


# get dummy variables whose are in categorical data
# for name in df.columns:
#     if df[name].dtype != "int64":
#         df[name] = pd.get_dummies(df[name]) 


# In[32]:


df.shape


# In[33]:


df.head()


# In[34]:


df.shape


# In[35]:


# split data into train and test
def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[36]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)


# In[37]:


train_data.head()


# In[ ]:





# In[38]:


train_data.shape


# In[39]:


test_data.shape


# In[40]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.Target
    return df.drop('Target', axis=1), output


# In[41]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[42]:


train_data_x.shape


# In[43]:


test_data_x.shape


# In[44]:


import random
import math
import operator


class KNN_Algorithm:
    def __init__(self):
        self.k = 5
        
#     calculate distance between two data instance
    def euclidien(self,test,train,test_lenth):
        distance = 0
        for l in range(test_lenth):
            distance += pow(test[l]-train[l],2)
#         print("distance",distance)
        return math.sqrt(distance)
        
#         get neighbors having atleast distance from new point
    def find_neighbours(self,x_train_data,y_train_data,x_test_data, k):
        distances = []
        test_lenth = len(x_test_data)-1
        for i in range(len(x_train_data)):
            dist = self.euclidien(x_test_data,x_train_data[i],test_lenth)
            distances.append((y_train_data[i],dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors =  []
        for k in range(k):
            neighbors.append(distances[k][0])
#         print("neighbor",neighbors)
        return neighbors
        
        
#       get response and decide which class it belongs 
    def getResponse(self,neighbors):
        classVotes = {}
#         print("neigh:",neighbors)
        for x in range(len(neighbors)):
            response = neighbors[x]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
                
#             print("CLASS :",classVotes)
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
#         print("sortedVotes",sortedVotes)
        return sortedVotes[0][0]
#         return classVotes[0][0]
    
#     calculate accuracy
    def getAccuracy(self,y_test_data, predictions):
        correct = 0
        for y in range(len(y_test_data)):
            if y_test_data[y] == predictions[y]:
                correct += 1
        return (correct/float(len(y_test_data))) * 100.0
        
        
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
    k = 5
    for x in range(len(x_test_data)):
        neighbors = obj.find_neighbours(x_train_data,y_train_data,x_test_data[x], k)
        result = obj.getResponse(neighbors)
        predictions.append(result)
#         print('> predicted=' + repr(result) + ', actual=' + repr(y_test_data[x]))
    accuracy = obj.getAccuracy(y_test_data, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

    
main()


# In[ ]:




