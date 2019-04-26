#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt


# In[83]:


# load dataset
df=pd.read_csv("Churn_Modelling.csv",delimiter=',')
df.head()


# In[84]:


# display columns in dataset
df.columns


# In[85]:


df.dtypes


# In[86]:


# display shape of dataset
print('dataset has {0} rows  and {1} column'.format(df.shape[0],df.shape[1])) 


# In[87]:


df.info()


# In[88]:


# checking missing values
df.columns[df.isnull().any()]


# In[89]:


target = df.skew()
sb.distplot(target)


# In[90]:


df['Exited'].value_counts()


# In[91]:


# plot subscription of yes and no
sb.countplot(x='Exited',  data=df, palette='hls')
plt.show()


# In[92]:


df.duplicated().sum()


# In[93]:


corr = df.corr()
sb.heatmap(corr)


# In[94]:


df.drop('Surname',axis=1, inplace=True)


# In[95]:


# categorical data encoding 
df = pd.get_dummies(df)
df.head()


# In[96]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[97]:


df = Feature_Scaling(df)


# In[98]:


df.head()


# In[99]:


df.shape


# In[100]:


# split data into train and test
def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[101]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)


# In[102]:


train_data.head()


# In[103]:


train_data.shape


# In[104]:


test_data.shape


# In[105]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.Exited
    return df.drop('Exited', axis=1), output


# In[106]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[107]:


train_data_x.shape


# In[108]:


train_data_y.shape


# In[109]:


test_data_x.shape


# In[110]:


test_data_y.shape


# In[111]:


class Neural_Network:
    def __init__(self):
        self.alpha = 0.001
        self.epoch = 10000
        
#         Traing the model
    def Train(self, x_data_train, y_data_train, weights, bias):
        db=0.0
        dw=0.0
        
        for length in range(self.epoch):
#         hypothesis function
            z = np.dot(weights.T,x_data_train.T)+bias
#         sigmoid function
            activation = (1/(1+np.exp(-z)))
#         calculating difference between activation and y_data_train
            dz = np.subtract(activation,y_data_train.T)
            temp_dw = np.dot(x_data_train.T,dz.T)
#         sumation of dz values
            temp_db = np.sum(dz,axis=1,keepdims=True)
#         derivatives of weights
            dw = np.divide(dw,len(x_data_train))
            db = np.divide(temp_db,len(x_data_train))
            temp_weights = np.dot(self.alpha,dw)
#         getting weights  values
            weights = np.subtract(weights,temp_weights)
            temp_bais =  np.dot(self.alpha,db)
#         getting bias value
            bias  = np.subtract(bias,temp_bais)
        return weights ,bias
    
#     classify the Train model 
    def classify(self, x_data_test, weights,bias):
        y_prediction = np.zeros((x_data_test.shape[0], 1), dtype=float)
        z = np.dot(x_data_test, weights)+ bias 
        sigmoid = np.array(1 / (1 + np.exp(-z)))
#         print("sigmoid shape:",sigmoid.shape)
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
    y_train_data = np.array(train_data_y)
    y_train_data = y_train_data.reshape(len(y_train_data),1)

    x_test_data = np.array(test_data_x)
    y_test_data = np.array(test_data_y)
    y_test_data=y_test_data.reshape(len(y_test_data),1)
    
#     initializing parameters
    weights = 14
    bias = 1
    
    weights = np.full((weights +  bias,1),.1)
#     passing parameters to train the model
    weights, bias = obj.Train(x_train_data, y_train_data,weights,bias)
    
#     testing our train model to make prediction over  
    y_predict_test = obj.classify(x_test_data, weights,bias)
    
#     testing our train model to make prediction over  
    y_predict_train = obj.classify(x_train_data,weights, bias)

#     get accuracy of train by comparing predicted data and actual data
    train_accuracy=obj.accuracy(y_train_data, y_predict_train)
    test_accuracy=obj.accuracy(y_test_data, y_predict_test)
    
    print("\nAccuracy Train:", train_accuracy)
    print("Accuracy Test:",  test_accuracy)

if __name__ == '__main__':
    main()


# In[ ]:




