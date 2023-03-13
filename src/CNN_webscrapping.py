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
       
"""Because of the specific code to do CNN website, a function is implemented to, first, start the browser and open the cnn website for, after accepting the cookies and using the search bar placed in it to search the word introduced in the function with Selenium. Because of the use of a VPN, the cookies might not be required to accept, so, for this reason it's used a try and except method to avoid errors, depending on the region of the VPN; on the other side, it's used a while loop which includes to get all the elements which tag is 'a' and attribute 'href', to get all the url links of the list of news; to be sure that it's downloaded just news it's applied an if method which has to include 'https://www.cnn.com/202' in the url. Once it's got the proper url this one is saved in a list out of the loop and it's extracted the title, the content and the date split in day, month and year with Beautifulsoup and saved in a dictionary with key the name of the column and the value the content. During the while, it's also introduced another Selenium method with a try and except, so, if the condition is not met, which can be a news without a proper date format, there's no 'more' button (which means the search in the website finished), or, the length of the list of news is not reach, pass.
It's also to include in the description the use of selenium to scroll down on the website until finding the button 'more' to continue downloading content."""
    
    url='https://edition.cnn.com'
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(3)
    try:
        cookies_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    except:
        pass
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




