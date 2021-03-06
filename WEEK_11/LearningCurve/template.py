import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt  
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from collections import defaultdict
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
        return x,ss
    
    def one_hot_encode(self,x_data):
        # from collections import defaultdict
        d = defaultdict(LabelEncoder)
        # Encoding the variable
        fit = x_data.apply(lambda x: d[x.name].fit_transform(x))
        # Inverse the encoded
        fit.apply(lambda x: d[x.name].inverse_transform(x))
        # Using the dictionary to label future data
        x_data.apply(lambda x: d[x.name].transform(x))
        one_hot_encode = OneHotEncoder()
        one_hot_encode.fit(x_data)
        x_data=one_hot_encode.transform(x_data).toarray()
        return x_data
    
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
        
#     fitting SVM classification model
    def Fit_Model_SVM(self,x,y):
        classifier = SVC(kernel='linear',random_state=0, probability=True)
        classifier.fit(x,y)
        return classifier
    
#     fitting decision tree classification model
    def Fit_Model_DecisionTree(self,x,y):
        classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
        classifier.fit(x,y)
        return classifier
    
#     fitting RandomForest classification model
    def Fit_Model_RandomForest(self,x,y):
        classifier = RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
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
