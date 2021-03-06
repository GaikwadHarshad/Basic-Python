#!/usr/bin/env python
# coding: utf-8

# In[57]:


# import libraries
import numpy as  np
import pandas as pd
import  array
import matplotlib.pyplot as plt
import importlib.util
from matplotlib.colors import ListedColormap
from  sklearn.preprocessing import LabelEncoder, OneHotEncoder
from  sklearn.preprocessing import StandardScaler
import array
import sklearn
import pickle
from sklearn.metrics import confusion_matrix
import warnings
import csv
warnings.filterwarnings('ignore')


# In[58]:


# importing template file 
spec = importlib.util.spec_from_file_location("Template", "/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_10/UtilityTemplate/UtilTemplate.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
# creating object of Template class
log_template = foo.Template()


# In[59]:


# importing dataset
dataset = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_10/Logistic Regression/Datasets/newHIV-1_data/1625Data.txt',header=None, names=['octamers','flag'])


# In[60]:


dataset.head()


# In[61]:


print("Dataset has {} rows and {} Columns".format(dataset.shape[0],dataset.shape[1])) 


# In[62]:


dataset.sample()


# In[63]:


# checking information about dataset
dataset.info()


# In[64]:


dataset.describe().T


# In[65]:


# checking null values in dataset
dataset.isnull().sum()


# In[66]:


# check for minimum dataset
dataset.min()


# In[67]:


# Seperate all amino acids
peptides = np.array([[dataset["octamers"][i][j] for i in range(dataset.shape[0])] for j in range(8)])
dataset.shape    


# In[68]:


print(peptides)


# In[69]:


# store seperated amino's in dataset
dummy = pd.DataFrame(peptides.T,columns=list("ABCDEFGH"))
# drop column octamers
dataset =dataset.drop(columns=['octamers'])
# concatenate datasetwith dummy data
dataset  = pd.concat([dummy,dataset],axis=1)
dataset.head()


# In[70]:


# split dataset into train and test set
train,test  =  log_template.split_datasets(dataset,0.33)
train.shape,test.shape


# In[71]:


# saving train and test data into csv file
train_csv = log_template.save_csv(train,'CSV_Files/train.csv')
test_csv = log_template.save_csv(test,'CSV_Files/test.csv')


# In[72]:


# reading train data from csv file
train = log_template.read_csv('CSV_Files/train.csv')


# In[73]:


# seperate label and features
x =  train.iloc[:,:-1].values
y = train.iloc[:,8].values
x.shape,y.shape


# In[74]:


x = pd.DataFrame(x)
type(x)


# In[75]:


# one hot encoding on x data
x = log_template.one_hot_encode(x)


# In[76]:


x.shape


# In[77]:


# encode dependent variable      
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)


# In[78]:


# feature scaling on x 
x,scale_obj = log_template.feature_scaling(x)


# In[79]:


x.shape


# In[80]:


log_template.save_csv(train,'CSV_Files/train.csv')


# In[81]:


train = log_template.read_csv('CSV_Files/train.csv')
# spliting train data in training and cross validation
train_data, cross_val  =  log_template.split_datasets(train,0.33)


# In[82]:


# saving cross_val data in csv file
cv_csv = log_template.save_csv(cross_val,'CSV_Files/cross_validation.csv') 


# In[83]:


# reading cross validation file  and perform operation on it

cv_file = log_template.read_csv('CSV_Files/cross_validation.csv')
cv_file.shape
# seperate label and features
x_cv =  cv_file.iloc[:,:-1].values
y_cv = cv_file.iloc[:,8].values
# converting x_cv to dataframe
x_cv = pd.DataFrame(x_cv)
type(x_cv)
# one hot encoding  on x_cv
x_cv = log_template.one_hot_encode(x_cv)
# encode dependent variable      
label_encoder_y = LabelEncoder()
y_cv = label_encoder_y.fit_transform(y_cv)
# feature scaling on x 
x_cv,scale_obj = log_template.feature_scaling(x_cv)
x_cv.shape


# In[84]:


class Training_Logistic_Model2():
    
    def fit_model(self,x,y):
        return log_template.Fit_Model_Logistic(x,y)
    
    def prediction(self,train,classifier):
        return  log_template.prediction(train,classifier)
    
    def get_confusion_matrix(self,train,predicted):
        return confusion_matrix(train,predicted)
        
    def get_accuracy(self,y,y_predicted):
        return  sklearn.metrics.balanced_accuracy_score(y,y_predicted)*100
        
        
def main():
# instantiation of class
    obj = Training_Logistic_Model2()
#     fitting train model
    classifier = obj.fit_model(x,y)
    print("Model Fitted")
#     prediction over train model by x_train data
    prediction_train = obj.prediction(x,classifier)
#     confusion matrix for describe performance of classification model
    train_cf_matrix = obj.get_confusion_matrix(y,prediction_train)
    print("Model performane on train data:\n",train_cf_matrix)

#     predict cross validation on model
    prediction_cv =  obj.prediction(x_cv,classifier)
    cv_cf_matrix  = obj.get_confusion_matrix(y_cv,prediction_cv)
    print("Model performance on cross validation:\n",cv_cf_matrix)
    
#     getting accuracy on train data  and cross validation
    train_accuracy = obj.get_accuracy(y,prediction_train)
    print("Accuracy on Train:",train_accuracy)
    cv_accuracy = obj.get_accuracy(y_cv,prediction_cv)
    print("Accuracy on cross validation:",cv_accuracy)
    
    # Setting threshold limit where we get accuracy greater than 80%
    # then save our model in pickle file  
    if train_accuracy or cv_accuracy > 80:
        file = open('Pickle File/TrainPickle.pkl', 'wb')
        pickle.dump(classifier,file)
        pickle.dump(scale_obj,file)
        file.close()     

if __name__ == '__main__':
    main()


# In[ ]:




