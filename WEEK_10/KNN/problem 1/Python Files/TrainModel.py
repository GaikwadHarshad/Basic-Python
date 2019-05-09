#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import numpy as  np
import pandas as pd
import  array
import matplotlib.pyplot as plt
import importlib.util
from matplotlib.colors import ListedColormap
import array
import sklearn
import pickle
from sklearn.metrics import confusion_matrix
import warnings
import csv
warnings.filterwarnings('ignore')


# In[2]:


# importing template file 
spec = importlib.util.spec_from_file_location("Template", "/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_10/UtilityTemplate/UtilTemplate.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
# creating object of Template class
log_template = foo.Template()


# In[3]:


# importing datasets
dataset = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_10/Logistic Regression/Datasets/Social_Network_Ads.csv')


# In[4]:


dataset.head()


# In[5]:


print("Dataset has {} rows and {} Columns".format(dataset.shape[0],dataset.shape[1])) 


# In[6]:


dataset.sample()


# In[7]:


# checking information about dataset
dataset.info()


# In[8]:


dataset.describe().T


# In[9]:


# checking null values in dataset
dataset.isnull().sum()


# In[10]:


# check for minimum dataset
dataset.min()


# In[11]:


# # split dataset into train and test set
train,test  =  log_template.split_datasets(dataset,0.20)
train.shape,test.shape


# In[12]:


# saving train data in csv file
train_csv  =  log_template.save_csv(train,'CSV_Files/train.csv')


# In[13]:


# saving test data in csv file
test_csv =  log_template.save_csv(test,'CSV_Files/test.csv')


# In[14]:


# reading train.csv for further operation on it
train_file  = log_template.read_csv('CSV_Files/train.csv')


# In[15]:


# Split train.csv data into Train and cross validation 
train_data,cross_val = log_template.split_datasets(train_file,0.30)


# In[16]:


train_data.shape,cross_val.shape


# In[17]:


# saving cross validation data in csv file
cv_file = log_template.save_csv(cross_val,'CSV_Files/cross_validation.csv')


# In[18]:


# reading cross validation file
cv_data = log_template.read_csv('CSV_Files/cross_validation.csv')


# In[19]:


# seperating features and label from train data
x_train = train_data.iloc[:,[2,3]].values
y_train = train_data.iloc[:,4].values


# In[20]:


# seperating features and label from cv data
x_cv = cv_data.iloc[:,[2,3]].values
y_cv = cv_data.iloc[:,4].values


# In[21]:


# reshape y column of train data
# y_train =y_train.reshape(-1,1)
x_train.shape,y_train.shape


# In[22]:


# reshape y column of  cv data
y_cv = y_cv.reshape(-1,1)
x_cv.shape,y_cv.shape


# In[23]:


# perform scaling operation on x train data
x_train,scale_obj = log_template.feature_scaling(x_train)


# In[ ]:


# perform scaling operation on x_cv of cross validation
x_cv,ss_cv = log_template.feature_scaling(x_cv)


# In[ ]:


class Training_K_Neighbors():
    
    def fit_model(self,x,y):
        return log_template.Fit_Model_KNN(x,y)
    
    def prediction(self,train,classifier):
        return  log_template.prediction_classifier(train,classifier)
    
    def get_confusion_matrix(self,train,predicted):
        return confusion_matrix(train,predicted)
        
    def get_accuracy(self,y,y_predicted):
        return  sklearn.metrics.balanced_accuracy_score(y,y_predicted)*100
        
    def visualization(self,x,y,classifier):
        x1,x2=np.meshgrid(np.arange(start=x[:,0].min()-1,stop=x[:,0].max()+1,step=0.01),np.arange(start=x[:,1].min()-1,stop=x[:,1].max()+1,step=0.01 ))
        plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))
        
        # limit the age and salary         
        plt.xlim(x1.min(),x1.max())
        plt.ylim(x2.min(),x2.max())
       
        # plots all the datapoints in graph         
        for i,j in enumerate(np.unique(y)):
            plt.scatter(x[y==j,0],x[y==j,1],c=ListedColormap(('orange','green'))(i),label=j)

        plt.title('K-Neighbors Model(Training  Set)')
        plt.xlabel('Age')
        plt.ylabel('estimated salary')
        plt.legend()
        plt.show()
        
def main():
# instantiation of class
    obj = Training_K_Neighbors()
#     fitting train model
    classifier = obj.fit_model(x_train,y_train)
    print("Model Fitted")
#     prediction over train model by x_train data
    prediction_train = obj.prediction(x_train,classifier)
#     confusion matrix for describe performance of classification model
    train_cf_matrix = obj.get_confusion_matrix(y_train,prediction_train)
    print("Model performane on train data:\n",train_cf_matrix)

#     predict cross validation on model
    prediction_cv =  obj.prediction(x_cv,classifier)
    cv_cf_matrix  = obj.get_confusion_matrix(y_cv,prediction_cv)
    print("Model performance on cross validation:\n",cv_cf_matrix)
    
#     getting accuracy on train data  and cross validation
    train_accuracy = obj.get_accuracy(y_train,prediction_train)
    print("Accuracy on Train:",train_accuracy)
    cv_accuracy = obj.get_accuracy(y_cv,prediction_cv)
    print("Accuracy on cross validation:",cv_accuracy)
    
    # Setting threshold limit where we get accuracy greater than 80%
    # then save our model in pickle file  
    if train_accuracy or cv_accuracy > 80:
        file = open('Pickle File/TrainPickle.pkl', 'wb')
#         dump classifier object in pickle file
        pickle.dump(classifier,file)
#     dump scale object of train data  in pickle  file
        pickle.dump(scale_obj,file)
        file.close()     

#     visualization of data
    obj.visualization(x_train,y_train,classifier)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




