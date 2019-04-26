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
df=pd.read_csv("classification_2.csv",delimiter=',')
df.head()


# In[3]:


# rename columns
df.columns=[
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial_Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital_Gain", "Capital_Loss",
        "Hours_per_week", "Country", "Target"]


# In[4]:


df.head()


# In[5]:


df['Education'].unique()


# In[6]:


df['Target'].unique()


# In[7]:


df.isnull().values.any()


# In[8]:


# replace value -1,1 for <=50K/>50K
df['Target'].replace(' <=50K',-1,inplace=True)
df['Target'].replace(' >50K',1,inplace=True)


# In[9]:


df.head()


# In[10]:


# display columns in dataset
df.columns


# In[11]:


df.dtypes


# In[12]:


# display shape of dataset
print('dataset has {0} rows and {1} column'.format(df.shape[0],df.shape[1]))


# In[13]:


df.info()


# In[14]:


# checking missing values
df.columns[df.isnull().any()]


# In[15]:


# getting target value greater  than 50k and less than 50k
df['Target'].value_counts()


# In[16]:


# plot Target of <=50k and >50k
sb.countplot(x='Education',  data=df, palette='hls')
plt.show()


# In[17]:


sb.countplot(x='Target',  data=df, palette='hls')
plt.show()


# In[18]:


df.duplicated().sum()


# In[19]:


# remove duplicated values from dataframe
df.drop_duplicates(keep=False, inplace=True)
df.duplicated().sum()


# In[20]:


df.shape


# In[21]:


# correlation of multivariate variable
# temp=df.corr(method='pearson')
# temp.head(11)
# corr['Target'].sort_values(ascending=False)[:]


# In[22]:


corr = df.corr()
sb.heatmap(corr)


# In[23]:


df.shape


# In[24]:


df.dtypes


# In[25]:


df = pd.get_dummies(df,columns=["Workclass","Education","Martial_Status","Occupation","Relationship", "Race", "Sex","Country"])
df.head()


# In[26]:


def Feature_Scaling(df):
        for column in df.columns:
            df[column] = ((df[column] - df[column].min()) /
                             (df[column].max() - df[column].min()))
        return df


# In[27]:


df = Feature_Scaling(df)


# In[28]:


# get dummy variables whose are in categorical data
# for name in df.columns:
#     if df[name].dtype != "int64":
#         df[name] = pd.get_dummies(df[name]) 


# In[29]:


df.shape


# In[30]:


df.head()


# In[31]:


df.shape


# In[32]:


# split data into train and test
def Split(data):
    train_set=0.70*len(data)
    train=int(train_set)
#         print(train)
    test_set=0.30*len(data)
    test=int(test_set)
        
    return train,test


# In[33]:


train,test = Split(df)
train_data=df.head(train)
test_data=df.tail(test)


# In[34]:


train_data.head()


# In[35]:


test_data.head()


# In[36]:


train_data.shape


# In[37]:


test_data.shape


# In[38]:


# Separating the output and the parameters data frame
def separate(df):
    output = df.Target
    return df.drop('Target', axis=1), output


# In[39]:


train_data_x,train_data_y = separate(train_data)
test_data_x,test_data_y=separate(test_data)


# In[40]:


train_data_x.shape


# In[41]:


test_data_x.shape


# In[51]:


class Multivariate_Logistic2:
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
    
    def accuracy(self, y_data_test, y_pred_test):
        count=0
        for i in range(0,len(y_data_test)):
            if y_pred_test[i]==y_data_test[i]:
                count = count + 1
        return count/len(y_data_test)*100
    
def main():
    obj = Multivariate_Logistic2()
    # calling method by class object
    
    x_train_data = np.array(train_data_x)
#     print("x_train_data:",x_train_data.shape)
    y_train_data = np.array(train_data_y)
    y_train_data = y_train_data.reshape(len(y_train_data),1)
#     print("y_train_data:",y_train_data.shape)

    
    x_test_data = np.array(test_data_x)
#     print("x_test_data:",x_test_data.shape)
    y_test_data = np.array(test_data_y)
    y_test_data=y_test_data.reshape(len(y_test_data),1)
#     print("y_test_data:",y_test_data.shape)
    
    
    x_train_data = np.column_stack((np.ones((x_train_data.shape[0], 1)), x_train_data))
    
    x_test_data = np.column_stack((np.ones((x_test_data.shape[0], 1)), x_test_data))
    
    x_size = 108
    theta_vector = np.full((x_size+1,1),.1)
#     print("theta vector:",theta_vector.shape)
    
    theta_vector = obj.Train(x_train_data, y_train_data,theta_vector)
#     print("theta vector:",theta_vector.shape)

    y_predict_test = obj.classify(x_test_data, theta_vector)
#     print("y_predict test:",y_predict_test.shape)
    
    y_predict_train = obj.classify(x_train_data, theta_vector)
#     print("y_predict train:",y_predict_train.shape)
    
    train_accuracy=obj.accuracy(y_train_data, y_predict_train)
    test_accuracy=obj.accuracy(y_test_data, y_predict_test)

    print("accuracy train:", train_accuracy)
    print("accuracy test:",  test_accuracy)
    
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




