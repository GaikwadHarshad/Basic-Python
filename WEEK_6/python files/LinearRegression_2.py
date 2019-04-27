#!/usr/bin/env python
# coding: utf-8

# In[43]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import pandas.api.types as  ptypes
# from google.colab import files
# uploaded = files.upload()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


# read weatherHistory.csv file
dataset = pd.read_csv("weatherHistory.csv")
dataset.head()


# In[45]:


dataset.dtypes


# In[46]:


# rename column Apparent Temperature
dataset.rename(columns={'Apparent Temperature (C)':'y','Humidity':'x'},inplace = True)


# In[47]:


# getting column x and y in dataset
dataset = dataset.loc[:,['y','x']]
dataset.head()


# In[48]:


dataset.describe()


# In[49]:


dataset.info()


# In[50]:


# calculating  sum of null values
dataset.isna().sum()


# In[51]:


# replace  NaN values with mean value
dataset.replace(np.NaN,dataset.mean(),inplace=True)


# In[52]:


# boxplot to  find outliers of datatset
sb.boxplot(data = dataset)


# In[53]:


def feature_scaling(dataset):
    for name in dataset.columns:
        dataset[name] = (dataset[name] - dataset[name].min()) / (dataset[name].max()-dataset[name].min())
    return dataset


# In[54]:


# feature  scaling
dataset = feature_scaling(dataset)


# In[55]:


# split dataset into train data and test data
def train_and_test_dataset(dataset):
#         calculate train dataset percentage for train model
        train_per = 0.70*len(dataset)
        train_per = int(train_per)
#         calculate test dataset percentage for test train model         
        test_per = len(dataset)-train_per
#         getting trained data from dataset
        X_train_set = dataset.head(train_per)
#         getting test data for testing train model
        Y_train_set = dataset.tail(test_per)
        return X_train_set,Y_train_set


# In[57]:


train,test = train_and_test_dataset(dataset)
train_data = train
test_data = test


# In[65]:


class LinearRegression:
    def gradient_descent(self,learning_rate,theta_0,theta_1,epoch,x_data,y_data):
        cost = np.empty(0)
        h1 = h2 =0
        fig = plt.figure()
        fig, (ax1, ax2, ax3,ax4) = plt.subplots(nrows=4, ncols=1, figsize=(5, 20))
        for i in  range(epoch):
            cost = 0
            h1 = 0.0
            h2 = 0.0
            cost_temp = 0.0
            for data  in range(len(x_data)):
                hypo = theta_0 + (theta_1 * x_data[data])
                h1 += (hypo - y_data[data])
                h2 += ((hypo - y_data[data]) * x_data[data])  
                cost += hypo - y_data[data]
    
#           getting minimum cost  function
            cost_temp +=(hypo - y_data[data]) ** 2 
            cost = (1/2 * len(x_data))* cost_temp
            theta_0 = theta_0 - ((learning_rate * h1) / len(x_data))
            theta_1 = theta_1 - ((learning_rate * h2) / len(x_data))
            
#             ploting graphs  on each 50 epochs 
            if(i%50 == 0):
               ax1.plot(i,theta_0,marker='o',color='r')
               ax1.set_title('iteration vs theta 0')
               ax2.plot(i,theta_1,marker='8',color='g')
               ax2.set_title('iteration vs theta 1')
               ax3.plot(i,cost,marker='*',color='b')
               ax3.set_title('iteration vs cost')
               ax4.plot(theta_0,theta_1,marker = 'x', color='black')
               ax4.set_title('theta_0 vs theta_1')
            if(cost<=0.00009): 
                break

        plt.subplots_adjust(hspace=1)
        plt.show()
        print("iteration = {} and cost function = {}".format(i, cost))
        return theta_0,theta_1

    def test(self, x_test_data, theta_0, theta_1):
        y_predict = [0]*len(x_test_data)
        for i in range(len(x_test_data)):
    #             y_predict[i] = theta_1*x_test_data[i] + theta_0
              y_predict[i] = (theta_0 + (theta_1*x_test_data[i]))
        return y_predict

    def accuracy(self, y_test_data, y_predicted):
        diff = 0
        for i in range(len(y_test_data)):
            diff += abs((y_predicted[i] - y_test_data[i])/y_test_data[i])
        diff  =  (diff/len(y_test_data))
        data_accuracy = 1 - diff
        return data_accuracy*100       



def main():
    obj =LinearRegression()
    learning_rate = 0.01
    theta_0 = 0.5
    theat_1 = 0.5
    epoch = 1000
    x_train_data = np.array(train_data["x"])
    y_train_data = np.array(train_data["y"])

    x_test_data = np.array(test_data["x"])
    y_test_data = np.array(test_data["y"])

#     calculate gradient descent on train data for test data
    t_0, t_1= obj.gradient_descent(learning_rate,theta_0,theat_1,epoch,x_train_data,y_train_data)
    print(t_0,t_1)

#     test data over train data 
    y_prediction_test =obj.test(x_test_data,t_0,t_1)

#     get accuracy of predicted value to original value
    accuracy = obj.accuracy(y_test_data,y_prediction_test)


    print("Accuracy:",accuracy)

if __name__ == '__main__':
    main()


# In[ ]:




