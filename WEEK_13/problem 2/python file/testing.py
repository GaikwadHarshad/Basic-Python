#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# reading test data from csv file for testing the  classier/trained model 
save_classifier = open("Test_data/test.pickle",'rb')
testing_set = pickle.load(save_classifier)
# save_classifier.close()


# In[3]:


type(testing_set)


# In[5]:


# reading trained model from pickle file
classifier_model = open("Pickle/naivebayes.pickle",'rb')
classifier =  pickle.load(classifier_model)


# In[6]:


# testing classifier model with classifier accuracy
print("Classifier test accuracy :",(nltk.classify.accuracy(classifier,testing_set)*100))


# In[7]:


save_classifier.close()

