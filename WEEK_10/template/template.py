import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt  
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import explained_variance_score
from sklearn.metrics import *
class Template:

    def split_dataset(dataset):
        x_train,x_test = train_test_split(dataset,test_size = 0.20)
        return x_train,x_test
    
    def split_data(x,y):
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20)
        return x_train,x_test,y_train,y_test
    
    def save_test_csv(test):
        return test.to_csv('test.csv',index=False)
    
    def save_train_csv(train):
        return train.to_csv('train.csv',index=False)
    
    def save_cv_csv(cv_data):
        return cv_data.to_csv('cross_valid.csv',index=False)
    
    def read_csv(file):
        data = pd.read_csv(file)
        return data
    
    def feature_scaling(x_cv):
        ss = StandardScaler()
        x_cv = ss.fit_transform(x_cv)
        return x_cv
    
    def Fit_Model(x,y):
        regressor = LinearRegression()
        regressor.fit(x,y)
        return regressor
        
    def prediction_train(x_test,regressor):
        y_predict_train = regressor.predict(x_test)
        return y_predict_train
    
    def prediction_cv(x_cv,regressor):
        y_predict_cv = regressor.predict(x_cv)
        return y_predict_cv
    
    def train_accuracy(y,y_predict_train):
        train_accuracy = explained_variance_score(y,y_predict_train)*100
        # train_accuracy = (1-train_accuracy)*100
        return train_accuracy
    
    def test_accuracy(y,y_predict_cv):
        test_accuraccy = explained_variance_score(y,y_predict_cv)
        test_accuraccy = (1-test_accuraccy)*100
        return test_accuraccy