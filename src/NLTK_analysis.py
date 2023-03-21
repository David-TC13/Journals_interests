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
    """ With this function, first of all needs to get a data frame and, also needs to import our personalised stopwords file which it's going to be used as a reference to analyse the key words. Once this first filter is applied, the second part gonna be to include the first 20 most used words in a list, to the reference it as a value in a dictionary for finally create a dataframe to merge with the original one. The result of it gonna be a new column called 'word' and each row is going to contain a list with those words. On the other side, it's going to include the polarity and the subjectivity in the same way: it's going to obtain the sentimental analysis (Subjectivity first and after the polarity) from each article and attach it in a new column on the DF, as a result of a dictionary with the key the name of the column and the value the list of values. At the end, for a future usage in the visualisation, it's created a new column with the full date separate by the character /."""   

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
    dict_subj={'subjectivity':list_subj}

    df_subj=pd.DataFrame(dict_subj)
    df_proc=pd.merge(df_proc,df_subj, left_index=True,  right_index=True)
    
    list_polar=[]
    for raw in df_raw['article']:
        blob = TextBlob(raw)
        polar = blob.sentiment.polarity
        list_polar.append(polar)
    dict_polar={'polarity':list_polar}

    df_polar=pd.DataFrame(dict_polar)
    df_together=pd.merge(df_proc,df_polar, left_index=True,  right_index=True)
    
    df_together['date']=df_together['day'].astype(str)+'/'+df_together['month'].astype(str)+'/'+df_together['year'].astype(str)
    return df_together

# In[3]:

def list_words(df):
    """This function returns the column word from the DF as a new DF which gonna return a single column with all the words to be used after for visualisation""" 
    lists_wds=df['word'].tolist()
    lst_wd=[j for i in lists_wds for j in i]
    dict_wd={'word':lst_wd}
    df_words= pd.DataFrame(dict_wd)
    return df_words



