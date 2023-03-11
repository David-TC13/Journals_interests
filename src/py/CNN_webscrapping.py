#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from dateutil import parser

import googletrans

import time
from datetime import datetime
import random

import requests
from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
import numpy as np

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

from wordcloud import WordCloud
from langdetect import detect
from textblob import TextBlob


# In[2]:


def keyword(word,no_news):
    
    url='https://edition.cnn.com'
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(3)
    cookies_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    
    time.sleep(3)
    search_button = driver.find_element(By.XPATH, "//button[@tabindex='-1']").click()
    search_bar  = driver.find_element(By.ID, 'header-search-bar')
    search_bar.send_keys(word)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    newest_button = driver.find_element(By.ID, 'newest').click()

    link_lst=[]
    try:
    
        while len(link_lst)<no_news: 
            time.sleep(5)
            lnks     = driver.find_elements(By.TAG_NAME,"a")
            lst_cnn  = [lnk.get_attribute('href') for lnk in lnks]
            lst_cnn_ = [link for link in list(set(lst_cnn)) if 'https://www.cnn.com/202' in str(link)]

            for i in lst_cnn_:
                link_lst.append(i)
                
                
            list_title=[]
            list_soup=[]
            for url in link_lst:
                html = requests.get(url)
                soup = BeautifulSoup(html.content, 'html.parser')
                title = soup.title.string
                article = soup.getText().replace('\n','').replace('      ','').replace('\xa0—\xa0','')
                list_soup.append(article)
                list_title.append(title)

            day_list=[]
            month_list=[]
            year_list=[]
            for url in link_lst:
                date_string = url.split("/")[3] + "-" + url.split("/")[4] + "-" + url.split("/")[5]
                dt_obj = parser.parse(date_string)

                day = dt_obj.day
                month = dt_obj.month
                year = dt_obj.year

                day_list.append(day)
                month_list.append(month)
                year_list.append(year)   
            more_button = driver.find_element(By.XPATH, "//div[@class='pagination-arrow pagination-arrow-right search__pagination-link text-active']")
            driver.execute_script("arguments[0].scrollIntoView();",more_button)
            more_button.click()
    
        dict_cnn={'title':list_title,
                'article': list_soup,
                 'link':link_lst,
                 'day':day_list,
                 'month': month_list,
                 'year': year_list}
        df_cnn=pd.DataFrame(dict_cnn)
        driver.close()

        return df_cnn

    except:
        pass


# In[ ]:




