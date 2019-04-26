#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt


# In[3]:


# read file
df_original=pd.read_csv("bank.csv",delimiter=";")
df =df_original


# In[4]:


df.head()


# In[5]:


x=df.iloc[:,:-1].values
print(x)


# In[6]:


# display columns in dataset
df.columns


# In[7]:


df.dtypes


# In[8]:


# display shape of dataset
print('dataset has {0} rows  and {1} column'.format(df.shape[0],df.shape[1])) 


# In[9]:


df.info()


# In[10]:


# checking missing values
df.columns[df.isnull().any()]


# In[11]:


target = df.skew()
sb.distplot(target)


# In[12]:


# replace value 1,0 for yes/no
df.replace(['yes','no'],[1,0],inplace=True)


# In[13]:


df.head()


# In[14]:


df['y'].value_counts()


# In[15]:


# plot subscription of yes and no
sb.countplot(x='y',  data=df, palette='hls')
plt.show()


# In[16]:


df.duplicated().sum()


# In[17]:


# df.drop(['month','marital','contact'], axis=1,inplace=True)


# In[18]:


# convert  categorical data into binary data
df = pd.get_dummies(df)
df.head()


# In[19]:


df.shape


# In[20]:


len(df.columns)


# In[21]:


# correlation of multivariate variable
temp=df.corr(method='pearson')
temp.head(11)


# In[22]:


df.shape


# In[23]:


# boxplot dataset
df.boxplot(rot=55, figsize=(20,5))


# In[24]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[25]:


df = Feature_Scaling(df)


# In[26]:


df.head()


# In[27]:


corr = df.corr()
sb.heatmap(corr)


# In[28]:


def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[29]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)
test_data.head()


# In[30]:


train_data.shape


# In[31]:


test_data.shape


# In[32]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.y
    return df.drop('y', axis=1), output


# In[33]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[34]:


test_data_x.tail()


# In[35]:


class Neural_Network:
    def __init__(self):
        self.alpha = 0.01
        self.epoch = 10000
        
    def Train(self, x_data_train, y_data_train, weights, bias):
        db=0.0
        for length in range(self.epoch):
#       hypothesis function
            z = np.dot(weights.T,x_data_train.T)+bias
#       sigmoid function  getting values between 0's and 1's
            activation = (1/(1+np.exp(-z)))
#      calculating difference between activation and y_data_train
            dz = np.subtract(activation,y_data_train.T)
            dw = np.dot(x_data_train.T,dz.T)
#       sumation of dz values
            db = np.sum(dz,axis=1,keepdims=True)
            dw = np.divide(dw,len(x_data_train))
            db = np.divide(db,len(x_data_train))
#       getting weights values
            temp_weights = np.dot(self.alpha,dw)
            weights = np.subtract(weights,temp_weights)
#       getting weights  values
            temp_bais =  np.dot(self.alpha,db)
            bias  = np.subtract(bias,temp_bais)
        return weights ,bias
    
#         classifing the Train model 
    def classify(self, x_data_test, weights,bias):
        y_prediction = np.zeros((x_data_test.shape[0], 1), dtype=float)
        z = np.dot(x_data_test, weights)+ bias 
        sigmoid = np.array(1 / (1 + np.exp(-z)))
        for i in (range(0, len(sigmoid))):
            if round(sigmoid[i][0],2) <= 0.5:
                y_prediction[i][0] = 0
            else:
                y_prediction[i][0] = 1
        return y_prediction
    
#     calculate accuracy of prediction over  output data
    def accuracy(self, y_data_test, y_pred_test):
        count=0
        for i in range(0,len(y_data_test)):
            if y_pred_test[i]==y_data_test[i]:
                count = count + 1
        return count/len(y_data_test)*100

def main():
#     class instantiation
    obj = Neural_Network()
    
    x_train_data = np.array(train_data_x)
    print("x_train_data:",x_train_data.shape)
    y_train_data = np.array(train_data_y)
    y_train_data = y_train_data.reshape(len(y_train_data),1)
    print("y_train_data:",y_train_data.shape)

    
    x_test_data = np.array(test_data_x)
    print("x_test_data:",x_test_data.shape)
    y_test_data = np.array(test_data_y)
    y_test_data=y_test_data.reshape(len(y_test_data),1)
    print("y_test_data:",y_test_data.shape)
    

#     initializing parameters
    weights = 47
    bias = 1
    
    weights = np.full((weights +  bias,1),.1)
    
#     passing parameters to train the model
    weights, bias = obj.Train(x_train_data, y_train_data,weights,bias)
    
#     testing our train model to make prediction over  
    y_predict_test = obj.classify(x_test_data, weights,bias)
    
#     testing our train model to make prediction over  
    y_predict_train = obj.classify(x_train_data,weights, bias)

#     get accuracy  by comparing prediction and actual output
    train_accuracy=obj.accuracy(y_train_data, y_predict_train)
    test_accuracy=obj.accuracy(y_test_data, y_predict_test)
    
    print("\nAccuracy Train:", train_accuracy)
    print("Accuracy Test:",  test_accuracy)

if __name__ == '__main__':
    main()


# In[ ]:




