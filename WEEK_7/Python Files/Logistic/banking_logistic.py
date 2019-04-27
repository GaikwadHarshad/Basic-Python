#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas.api.types as ptypes
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt


# In[2]:


# read file
df_original=pd.read_csv("bank.csv",delimiter=";")
df =df_original


# In[3]:


df.head()


# In[4]:


x=df.iloc[:,:-1].values
print(x)


# In[5]:


# display columns in dataset
df.columns


# In[6]:


df.dtypes


# In[7]:


# display shape of dataset
print('dataset has {0} rows and {1} column'.format(df.shape[0],df.shape[1]))


# In[8]:


df.info()


# In[9]:


# checking missing values
df.columns[df.isnull().any()]


# In[10]:


target = df.skew()
sb.distplot(target)


# In[11]:


# replace value 1,0 for yes/no
df.replace(['yes','no'],[1,0],inplace=True)


# In[12]:


df.head()


# In[13]:


df['y'].value_counts()


# In[14]:


# plot subscription of yes and no
sb.countplot(x='y',  data=df, palette='hls')
plt.show()


# In[15]:


df.duplicated().sum()


# In[16]:


# df.drop(['month','marital','contact'], axis=1,inplace=True)


# In[17]:


# convert  categorical data into binary data
df = pd.get_dummies(df)
df.head()


# In[18]:


df.shape


# In[19]:


len(df.columns)


# In[20]:


# correlation of multivariate variable
temp=df.corr(method='pearson')
temp.head(11)


# In[21]:


df.shape


# In[22]:


# boxplot dataset
df.boxplot(rot=55, figsize=(20,5))


# In[23]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[24]:


df = Feature_Scaling(df)


# In[25]:


df.head()


# In[26]:


corr = df.corr()
sb.heatmap(corr)


# In[27]:


def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[28]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)
test_data.head()


# In[29]:


train_data.shape


# In[30]:


test_data.shape


# In[31]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.y
    return df.drop('y', axis=1), output


# In[32]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[33]:


test_data_x.tail()


# In[38]:


class Multivariate_Logistic:
    def __init__(self):
        # loads csv file
        self.alpha = 0.1
        self.epoch = 10000
        
    def Train(self, x_data_train, y_data_train,theta_vector):
        for length in range(self.epoch):
            z = (np.dot(theta_vector.T,x_data_train.T))
#             print("z shape,",z.shape)
            sigmoid = (1/(1+np.exp(-z)))
#             print("sigmoid shape:",sigmoid.shape)
            diff = sigmoid - y_data_train.T
#             print("difference:",diff.shape)
            temp = np.dot(diff,x_data_train)
#             print("temp shape:",temp.shape)
            temp = np.divide(np.dot(self.alpha,temp),len(x_data_train))
#             print("temp diff shape:",temp.shape)
            theta_vector = theta_vector-temp.T
        return theta_vector
    
    def classify(self, x_data_test, theta_vector):
        y_prediction = np.zeros((x_data_test.shape[0], 1), dtype=float)
        z = np.dot(x_data_test, theta_vector)
        sigmoid = np.array(1 / (1 + np.exp(-z)))
        for i in (range(0, len(sigmoid))):
            if round(sigmoid[i][0],2) <= 0.5:
                y_prediction[i][0] = 0
            else:
                y_prediction[i][0] = 1
        return y_prediction
    
    
#     def accuracy(self, y_test_data, y_predict,y_predict_train,y_train_data):
#         # accuracy
#         train_accuracy = round(float(100 - np.mean(np.abs(y_predict_train - y_train_data)) * 100))
#         test_accuracy = round(float(100 - np.mean(np.abs(y_predict - y_test_data)) * 100))
#         return train_accuracy,test_accuracy
    def accuracy(self, y_data_test, y_pred_test):
        count=0
        for i in range(0,len(y_data_test)):
            if y_pred_test[i]==y_data_test[i]:
                count = count + 1
        return count/len(y_data_test)*100

def main():
    obj = Multivariate_Logistic()
    # calling method by class object
    list1 = []
    
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
    
    
    x_train_data = np.column_stack((np.ones((x_train_data.shape[0], 1)), x_train_data))
    
    x_test_data = np.column_stack((np.ones((x_test_data.shape[0], 1)), x_test_data))
    
    x_size = 48
    theta_vector = np.full((x_size+1,1),.1)
    print("theta vector:",theta_vector.shape)
    
    theta_vector = obj.Train(x_train_data, y_train_data,theta_vector)
#     print(theta_vector)
    print("theta vector:",theta_vector.shape)
    
    y_predict_test = obj.classify(x_test_data, theta_vector)
#     print(y_predict_test)
    print("y_predict test:",y_predict_test.shape)
    
    y_predict_train = obj.classify(x_train_data,theta_vector)
#     print(y_predict_train)
    print("Y_predict train:",y_predict_train.shape)
    
    train_accuracy=obj.accuracy(y_train_data, y_predict_train)
    test_accuracy=obj.accuracy(y_test_data, y_predict_test)

#     train_accuracy,test_accuracy = obj.accuracy(y_test_data, y_predict_test,y_predict_train,y_train_data)
    print("\naccuracy train:", train_accuracy)
    print("accuracy test:",  test_accuracy)

if __name__ == '__main__':
    main()
    


# In[ ]:





# In[ ]:




