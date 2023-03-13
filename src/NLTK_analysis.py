#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests

from bs4 import BeautifulSoup
import re

from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# In[2]:


def preprocess(df_raw):
    raw_list= df_raw['article']
    list_text = []
    
    stop_words_file = 'english.txt'
    stop_words = []

    with open(stop_words_file, "r") as f:
        for line in f:
            stop_words.extend(line.split()) 
    for raw_text in raw_list:
        stop_words = stop_words  
        letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

        words = letters_only_text.lower().split()

        cleaned_words = []


        for word in words:
            if word not in stop_words:
                cleaned_words.append(word)
        cleaned_text = " ".join(cleaned_words)
        list_text.append(cleaned_text)

    dict_words = {}

    for i, text in enumerate(list_text):
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        words = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
        word_freq = Counter(words)
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        list_word = []
        for word, freq in sorted_words[:20]:
            list_word.append(word)
        dict_word={'word':list_word}

        dict_words[i] = dict_word


    df_words=pd.DataFrame(dict_words).T
    df_proc=pd.merge(df_raw,df_words, left_index=True,  right_index=True)
    
    list_subj=[]
    for raw in df_raw['article']:
        blob = TextBlob(raw)
        subj = blob.sentiment.subjectivity
        list_subj.append(subj)
    dict_subj={'subjetivity':list_subj}

    df_subj=pd.DataFrame(dict_subj)
    df_together=pd.merge(df_proc,df_subj, left_index=True,  right_index=True)

    return df_together


# In[ ]:




