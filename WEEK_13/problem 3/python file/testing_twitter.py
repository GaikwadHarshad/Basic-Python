#!/usr/bin/env python
# coding: utf-8

# In[20]:


import nltk
import pickle
from sklearn.metrics import f1_score
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[16]:


test_tweet = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_13/Datasets/test_tweets.csv') 


# # Testing Model with stemmed Tweets

# In[12]:


# reading test_stem.pickle file for testing
test_pickle = open('Test_data/stem_test.pickle','rb')
test_set = pickle.load(test_pickle)
test_pickle.close()


# In[13]:


# Loading trained Stem Model
model  =  open('Pickle/StemModel.pickle','rb')
classifier = pickle.load(model)
transformed = pickle.load(model)
model.close()


# In[17]:





# In[22]:



# predicting on the validation set
prediction = classifier.predict_proba(test_set) 
# if prediction is greater than or equal to 0.3 than 1 else 0
prediction_int = prediction[:,1] >= 0.3 
prediction_int = prediction_int.astype(np.int)
# calculating f1 score on validation data
score = f1_score(test_set, prediction_int) 


# In[18]:


# print("Classifier test accuracy :",(nltk.classify.accuracy(classifier,test_set)*100))


# In[ ]:




