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
from datetime import datetime

import googletrans

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

    url = 'https://www.rt.com'
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get(url)       
    
    cookies= driver.find_element(By.PARTIAL_LINK_TEXT,'Accept cookies').click()
    
    search_bar = driver.find_element(By.CLASS_NAME, "js-search-input")
    search_bar.send_keys(word)
    search_bar.send_keys(Keys.RETURN)

    lst_link=[]
    try:

        while len(lst_link)< no_news:
            lnks       = driver.find_elements(By.TAG_NAME,"a")
            lst_rt     = [lnk.get_attribute('href') for lnk in lnks]
            lst_rt_1   = [url for url in lst_rt if 'https://www.rt.com/news/5' in str(url)]
            lst_link   = [i for i in lst_rt_1]

            lst_link=list(set(lst_link))

            list_soup = []
            list_title=[]
            for url in lst_link:
                html  = requests.get(url)
                soup  = BeautifulSoup(html.content, "html.parser")
                title_element = soup.find('title')
                title = title_element.text
                list_soup.append(soup)
                list_title.append(title)
                
            art_list = []  
            for soup in list_soup:
                article = soup.getText()
                article = article[article.find('Home'):]
                article = article[:article.find('You can share this story on social media:')]
                article = article.replace('\xa0','').replace('\n','').replace('READ MORE','').replace('/','').replace('HomeWorld News','')
                art_list.append(article)

            day_list=[]
            month_list=[]
            year_list=[]
            year_control=[]

            for soup in list_soup:
                date_str = soup.find('span', {'class': 'date'}).text.strip()
                day, month, year, time = date_str.split()
                day = day.zfill(2)
                month = month.zfill(2).replace(',','')
                year= year

                day_list.append(day)
                month_list.append(month)
                year_list.append(year)
                
            more_button= driver.find_element(By.ID,'listingBtn')
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)",more_button)
            more_button.click()

        dict_={'title':list_title,
                'article': art_list,
                'link': lst_link,            
                'year' : year_list,
                'month': month_list,
                'day': day_list
                }
        df= pd.DataFrame(dict_)
        driver.close()
        return df
    
    except:
        pass

