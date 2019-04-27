#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[62]:


# load dataset
df=pd.read_csv("Churn_Modelling.csv",delimiter=',')
df.head()


# In[63]:


# display columns in dataset
df.columns


# In[64]:


df.dtypes


# In[65]:


# display shape of dataset
print('dataset has {0} rows  and {1} column'.format(df.shape[0],df.shape[1])) 


# In[66]:


df.info()


# In[67]:


# checking missing values
df.columns[df.isnull().any()]


# In[68]:


target = df.skew()
sb.distplot(target)


# In[69]:


df['Exited'].value_counts()


# In[70]:


# plot subscription of yes and no
sb.countplot(x='Exited',  data=df, palette='hls')
plt.show()


# In[71]:


df.duplicated().sum()


# In[72]:


corr = df.corr()
sb.heatmap(corr)


# In[73]:


df.drop('Surname',axis=1, inplace=True)


# In[74]:


# categorical data encoding 
df = pd.get_dummies(df)
df.head()


# In[75]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[76]:


df = Feature_Scaling(df)


# In[77]:


df.head()


# In[78]:


df.shape


# In[79]:


# split data into train and test
def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[80]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)


# In[81]:


train_data.head()


# In[82]:


train_data.shape


# In[83]:


test_data.shape


# In[84]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.Exited
    return df.drop('Exited', axis=1), output


# In[85]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[86]:


train_data_x.shape


# In[87]:


train_data_y.shape


# In[88]:


test_data_x.shape


# In[89]:


test_data_y.shape


# In[90]:


class Multi_Neural_Network:
    def __init__(self):
        self.alpha = 0.1
        self.epoch = 1000
        
    def Train(self, x_data_train, y_data_train):
        Layers =[x_data_train.shape[1], 4, 5, 3, 1]
        a = [0] * len(Layers)
#         a = np.zeros(len(Layers),1)
        a[0] = x_data_train.T
        z = [0] * len(Layers)
        A = [0] *len(Layers)
        dg = [0] * len(Layers)
        dw = [0] * len(Layers)
        db = [0] * len(Layers)
        dz = [0] * len(Layers)
        da = [0] * len(Layers)
        weights = []
        bias = []
        
#         initialization of weights and bias
        for i in range(0,len(Layers)):
            weights.append(np.random.rand(Layers[i],Layers[i-1]) * 0.001)
            bias.append(np.zeros((Layers[i],1)))
            
#   weights and bias  shape
        print("Initial weights:",len(weights))
        print("Initial biased:",len(bias))
        
        for length in range(self.epoch):
        ############ forward propagation  ##################
            for i in range(1,len(Layers)):
                z[i] = np.dot(weights[i], a[i-1]) + bias[i]
                a[i] = (1/(1+np.exp(-z[i])))
    
        ############# Backward propagation #################
            for j in reversed(range(1,len(Layers))):
                # hidden layers 
                da[j] = (-(y_data_train.T/a[j]) + ((1-y_data_train.T/(1-a[j]))))
                dg[j] = (1 / (1 + np.exp(-z[j]))) * (1 - (1 / (1 + np.exp(-z[j]))))
                dz[j] = da[j]*dg[j]
                dw[j] = np.dot(dz[j],a[j-1].T)/len(x_data_train)
                db[j] = np.sum(dz[j], axis =1 ,keepdims = True) / len(x_data_train)
                weights[j] = weights[j] - (self.alpha*dw[j])
                bias[j] =  bias[j] - (self.alpha*db[j])
        return weights,bias
    
#         classifing the Train model 
    def classify(self, x_data_test, parameters):
        Layers =[x_data_test.shape[1], 4, 5, 3, 1]
        z = [0] * len(Layers)
        a = [0] * len(Layers)
        a[0] = x_data_test.T
        for i in range(1,len(Layers)):
            z[i] = np.dot(parameters[0][i], a[i-1]) + parameters[1][i]
            a[i] = (1 / (1 + np.exp(-z[i]))) 
        return a[-1]

#     calculate accuracy of prediction over  output data
    def accuracy(self, y_data_test, y_pred_test):
        y_pred_test = np.nan_to_num(y_pred_test)
        test_accuracy = 100 - (np.mean(np.abs(y_pred_test - y_data_test)) * 100)        
        return test_accuracy

def main():
#     class instantiation
    obj = Multi_Neural_Network()
    
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
    
#     passing parameters to train the model
    parameters = obj.Train(x_train_data, y_train_data)
    print("weights After Training Model:",parameters[0][0].shape)
    print("Bias After Training  Model:",parameters[0][1].shape)
#     testing our train model to make prediction over  
    y_predict_test = obj.classify(x_test_data,parameters)
    print("y predict test:",y_predict_test.shape)
# #     testing our train model to make prediction over  
    y_predict_train = obj.classify(x_train_data, parameters)
    print("Y predict train:",y_predict_test.shape)

#     get accuracy  by comparing prediction and actual output
    train_accuracy=obj.accuracy(y_train_data, y_predict_train)
    test_accuracy=obj.accuracy(y_test_data, y_predict_test)
    
    print("\nAccuracy Train:", train_accuracy)
    print("Accuracy Test:",  test_accuracy)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:



