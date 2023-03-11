#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[5]:


def keyword(word, no_news):
    
    url= 'http://en.people.cn'
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(3)
    cookies_button_deny  = driver.find_element(By.CLASS_NAME,'tipsClose').click()

    form = driver.find_element(By.NAME,"searchFormForPC")
    keyword_input = form.find_element(By.NAME,"keyword")
    keyword_input.send_keys(word)
    keyword_input.send_keys(Keys.RETURN)
    driver.close()
    
    driver.switch_to.window( driver.window_handles[0])
    
    link_lst=[]
    
    while len(link_lst)<no_news:

        lnks          = driver.find_elements(By.TAG_NAME,"a")
        lst_pc        = [lnk.get_attribute('href') for lnk in lnks]
        lst_pc_       = [url for url in lst_pc if '/2023' in url or '/2022'in url]
        for i in lst_pc_:
            link_lst.append(i)
            
        link_lst= list(set(link_lst))

        list_soup=[]
        list_title=[]

        for url in link_lst:
            html    = requests.get(url)
            soup    = BeautifulSoup(html.content, "html.parser")
            title   = soup.title.string.strip()
            article = soup.getText()
            article = article[:article.find('(Web editor')]
            article = article[article.find('>>'):]
            article=article.replace('\n','').replace('\t','').replace('\'s',"´s").replace('>>',"")
            list_soup.append(article)
            list_title.append(title)
            

        day_list=[]
        month_list=[]
        year_list=[]
        for url in link_lst:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            date_div = soup.find('div', class_='origin')
            date_str = date_div.span.text.strip()

            hour, month_day, year = date_str.split(", ")[-3:]
            month_str, day = month_day.split(" ")

            months_dict = {
                'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9,
                'October': 10,
                'November': 11,
                'December': 12
            }
            month_int = months_dict[month_str]

            day_list.append(day)
            month_list.append(month_int)
            year_list.append(year)
            
            try:
                next_button = driver.find_element(By.LINK_TEXT, 'Next').click()
            except:
                pass
        
    dict_pc={'title': list_title,
         'article':list_soup,
         'link': link_lst,
         'day':day_list,
         'month':month_list,
         'year':year_list
            }
    df_cn= pd.DataFrame(dict_pc)
    driver.close()
   
    return df_cn

