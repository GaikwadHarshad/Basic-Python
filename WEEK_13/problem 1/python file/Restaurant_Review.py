#!/usr/bin/env python
# coding: utf-8

# # Natural Language Processing

# In[1]:


# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as  pd
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import  confusion_matrix
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# import dataset
dataset = pd.read_csv('/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_13/Datasets/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)


# In[3]:


dataset.head()


# # Cleaning Text

# In[4]:


# download stopwords
nltk.download('stopwords')
corpus = []
for i in range(0,1000):
    # cleaning text
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    # convert capital letters  into lowercase
    review = review.lower()
    # spliting words from list of review
    review = review.split()
    # object of porterStemmer
    ps = PorterStemmer()
    # remove not relevent word in review and apply  stemming
    review = [ps.stem(word)  for  word in review if not word in set(stopwords.words("english"))]
    # join the review  words together 
    review = ' '.join(review)
    corpus.append(review)
    


# In[5]:


# display review list
for i in range(0,1000):
    print(corpus[i])


# # Bag of Word Model

# In[7]:


# Convert a collection of text documents to a matrix of token counts
cv = CountVectorizer(max_features=1500)
# fit and transform corpus to make sparse matrics for independent variable
X = cv.fit_transform(corpus).toarray()
# prepare dependent variable vector
y =  dataset.iloc[:,1].values


# # Training Model

# In[8]:


# splitting dataset into train and test set
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.20, random_state=0)
# train,test= train_test_split()


# In[9]:


# shapes of train set and test set
X_train.shape,X_test.shape,Y_train.shape,Y_test.shape


# In[10]:


# fitting naive bayes to training set
classifier = GaussianNB()
classifier.fit(X_train,Y_train)


# In[11]:


# predicting Test Set Result
y_prediction = classifier.predict(X_test)


# In[12]:


# Making confusion matrix
confusion_mat = confusion_matrix(Y_test,y_prediction)


# In[13]:


confusion_mat


# # Evaluating Performance of Model

# In[14]:


from sklearn.metrics import *
accuracy = accuracy_score(y_prediction,Y_test)*100
print("Model accuracy is {} %.".format(accuracy))
precision = precision_score(y_prediction,Y_test)*100
print("Precision is {} %.".format(round(precision,2)))
recall  = recall_score(y_prediction,Y_test)*100
print("Recall is {}  %".format(round(recall,2)))
# f1_score help to 
f1_score = f1_score(y_prediction,Y_test)*100
print("F1_score is {}  %".format(round(f1_score,2)))


# In[15]:


from sklearn.metrics import classification_report
performance = classification_report(y_prediction,Y_test)
print(performance)

