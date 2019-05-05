import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt  
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import explained_variance_score
from sklearn.metrics import *

class Template:

#     spliting dataset into train and test dataset
    def split_datasets(self,dataset,size):
        x_train,x_test = train_test_split(dataset,test_size=size)
        return x_train,x_test
    
#     split data into train x,y and test x,y dataset
    def split_data(self,x,y,test_size):
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size)
        return x_train,x_test,y_train,y_test
    
#     saving dataset into csv files
    def save_csv(self,dataset, path):
        return dataset.to_csv(path, index=False)

#     reading csv files
    def read_csv(self,path):
        data = pd.read_csv(path)
        return data
    
#     feature  scaling on x dataset
    def feature_scaling(self,x):
        ss = StandardScaler()
        x = ss.fit_transform(x)
        return x
    
#     fitting linear regression model
    def Fit_Model(self,x,y):
        regressor = LinearRegression()
        regressor.fit(x,y)
        return regressor
    
#     fitting logistic regression model
    def Fit_Model_Logistic(self,x,y):
        classifier = LogisticRegression()
        classifier.fit(x,y)
        return classifier
    
#     fitting k neighbors classification model
    def Fit_Model_KNN(self,x,y):
        classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2) 
        classifier.fit(x,y)
        return classifier
        
#    prediction over x data 
    def prediction(self,x_data,regressor):
        predicted = regressor.predict(x_data)
        return predicted

#    prediction over x data 
    def prediction_classifier(self,x_data,classifier):
        predicted = classifier.predict(x_data)
        return predicted
