#!/usr/bin/env python
# coding: utf-8

# # Movie Review

# In[1]:


# import libraries
import nltk
import random
import nltk
import numpy as np
import pickle
import pandas as pd
# downloading package movie reviews
nltk.download('movie_reviews') 
from nltk.corpus import movie_reviews


# In[2]:


documents = []
# getting +ve and -ve categories of movie
for category in movie_reviews.categories():
#     getting fileids of movie  having different categories
    for fileid in movie_reviews.fileids(category):
#         add that data/fileids into documents
        documents.append((list(movie_reviews.words(fileid)),category))


# In[3]:


# random shuffle data because we are going to training and testing data
random.shuffle(documents)


# In[4]:


# collecct all words, so we can have a massive list of typical words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
    
# perform frequency distribution to  find out  most common words
all_words = nltk.FreqDist(all_words)


# In[5]:


# converting words into features
words_features = list(all_words.keys())[:3000]


# In[6]:


# we will find features in our positive and negetive documents
def find_features(documents):
    words = set(documents)
    features = {}
    for w in words_features:
        features[w] = (w in words) 
    return features


# In[7]:


# cheking negetive documents words whether they're present in all_words document or not 
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))


# In[8]:


# saving feature existance boolean and their respective positive or negetive categories
featuresets = [(find_features(rev), category) for (rev, category) in documents]


# In[9]:


# set that we'll train our classifier with
training_set = featuresets[:1900]
# set that we'll test against
testing_set = featuresets[1900:]
# setting cross validation and train data from training set
train_data = training_set[:1800]
cross_val = training_set[1800:]
# converting testing_set in dataframe
# testing_set = pd.DataFrame(testing_set)


# In[10]:


np.asarray(train_data).shape


# In[11]:


# saving test data in seperate csv file for testing the  classier/trained model 
save_classifier = open("Test_data/test.pickle",'wb')
pickle.dump(testing_set,save_classifier)
save_classifier.close()


# In[16]:


# define and train our classifier
classifier = nltk.NaiveBayesClassifier.train(train_data)
# testing classifier model with classifier accuracy
print("Classifier accuracy :",(nltk.classify.accuracy(classifier,cross_val)*100))


# In[ ]:





# In[17]:


# Now we see what the most valuable words are when it comes to positive or negative reviews
classifier.show_most_informative_features(15)


# In[15]:


# now saving classifier object in pickle file or saving trained model
save_classifier = open("Pickle/naivebayes.pickle",'wb')
pickle.dump(classifier, save_classifier)
save_classifier.close()


# In[ ]:




