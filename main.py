#!/usr/bin/env python
# coding: utf-8

# # Main

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
import numpy as np

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# ## Webscrapping

# ### Importing BBC webscrapping

# In[2]:


import src.BBC_webscrapping as bbc


# In[3]:


df_bbc_russia = bbc.keyword('Russia',200)


# In[4]:


df_bbc_china = bbc.keyword('China',200)


# ### Importing CNN webscrapping

# In[2]:


import src.CNN_webscrapping as cnn


# In[3]:


df_cnn_russia = cnn.keyword('Russia',200)


# In[3]:


df_cnn_china = cnn.keyword('China',200)


# ### Importing Peoples's  Daily Online

# In[45]:


import src.peoples_webscrapping as pdo


# In[6]:


df_united_states = pdo.keyword('United States',60)


# In[8]:


df_usa = pdo.keyword('USA',60)


# In[9]:


df_pd_us=pd.concat([df_united_states,df_usa])


# In[46]:


df_uk = pdo.keyword('UK',60)


# In[49]:


df_united_kingdom = pdo.keyword('United Kingdom',60)


# In[50]:


df_pd_uk=pd.concat([df_uk,df_united_kingdom])


# ### Importing RT webscrapping

# In[27]:


import src.RT_webscrapping as rt


# In[21]:


df_united_states = rt.keyword('United States',100)


# In[29]:


df_usa = rt.keyword('USA',20)


# In[30]:


df_rt_us= pd.concat([df_united_states,df_usa])


# In[32]:


df_united_kingdom = rt.keyword('United Kingdom',100)


# In[37]:


df_united_kingdom.to_csv('rt_pre.csv')


# In[ ]:


df_uk = rt.keyword('uk',100)


# In[39]:


df_rt_uk=pd.concat([df_united_kingdom,df_uk])


# ## - not required- Saving raw data into CSV 

# In[6]:


df_bbc_china.to_csv('data/raw/bbc_china.csv',index=False)  


# In[5]:


df_bbc_russia.to_csv('data/raw/bbc_russia.csv',index=False)  


# In[4]:


df_cnn_china.to_csv('data/raw/cnn_china.csv',index=False)


# In[4]:


df_cnn_russia.to_csv('data/raw/cnn_russia.csv',index=False)


# In[10]:


df_pd_us.to_csv('data/raw/pdo_united_states.csv',index=False)  


# In[52]:


df_pd_uk.to_csv('data/raw/pdo_united_kingdom.csv',index=False)  


# In[32]:


df_rt_us.to_csv('data/raw/rt_united_states.csv',index=False)  


# In[42]:


df_rt_uk.to_csv('data/raw/rt_united_kingdom.csv',index=False)  


# ## Natural Languaje, Subjectivity and Polarity analysis

# ### Importing functions

# In[2]:


import src.NLTK_analysis as nk


# ### - Not required - Importing raw files

# In[3]:


df_bbc_china=pd.read_csv('data/raw/bbc_china.csv')


# In[4]:


df_bbc_russia=pd.read_csv('data/raw/bbc_russia.csv')


# In[5]:


df_cnn_china=pd.read_csv('data/raw/cnn_china.csv')


# In[6]:


df_cnn_russia=pd.read_csv('data/raw/cnn_russia.csv')


# In[7]:


df_pd_us=pd.read_csv('data/raw/pdo_united_states.csv')


# In[8]:


df_pd_uk=pd.read_csv('data/raw/pdo_united_kingdom.csv')


# In[9]:


df_rt_us=pd.read_csv('data/raw/rt_united_states.csv')


# In[10]:


df_rt_uk=pd.read_csv('data/raw/rt_united_kingdom.csv')


# ### Applying to BBC

# - China

# In[11]:


df_bbc_china = nk.preprocess(df_bbc_china)


# In[12]:


df_bbc_china.to_csv('data/processed/bbc_china_proc.csv',index=False)


# - Russia

# In[13]:


df_bbc_russia = nk.preprocess(df_bbc_russia)


# In[14]:


df_bbc_russia.to_csv('data/processed/bbc_russia_proc.csv',index=False)


# ### Applying to CNN

# - China

# In[15]:


df_cnn_china = nk.preprocess(df_cnn_china)


# In[16]:


df_cnn_china.to_csv('data/processed/cnn_china_proc.csv',index=False)


# - Russia

# In[17]:


df_cnn_russia = nk.preprocess(df_cnn_russia)


# In[18]:


df_cnn_russia.to_csv('data/processed/cnn_russia_proc.csv',index=False)


# ### Applying to People's Daily Online

# - United States of America

# In[19]:


df_pd_us = nk.preprocess(df_pd_us)


# In[20]:


df_pd_us.to_csv('data/processed/pdo_united_states_proc.csv',index=False)


# - United Kingdom

# In[21]:


df_pd_uk = nk.preprocess(df_pd_uk)


# In[22]:


df_pd_uk.to_csv('data/processed/pdo_united_kingdom_proc.csv',index=False)


# ### Applying to RT

# - United States of America

# In[23]:


df_rt_us = nk.preprocess(df_rt_us)


# In[24]:


df_rt_us.to_csv('data/processed/rt_united_states_proc.csv',index=False)


# - United Kingdom

# In[25]:


df_rt_uk = nk.preprocess(df_rt_uk)


# In[26]:


df_rt_uk.to_csv('data/processed/rt_united_kingdom_proc.csv',index=False)


# ### wordcloud

# In[27]:


import src.wordcloud as wc


# In[28]:


wc.wordcloud(df_bbc_russia)


# In[29]:


wc.wordcloud(df_bbc_china)


# In[30]:


wc.wordcloud(df_cnn_russia)


# In[31]:


wc.wordcloud(df_cnn_china)


# In[32]:


wc.wordcloud(df_pd_uk)


# In[33]:


wc.wordcloud(df_pd_us)


# In[34]:


wc.wordcloud(df_rt_uk)


# In[35]:


wc.wordcloud(df_rt_us)


# In[ ]:




