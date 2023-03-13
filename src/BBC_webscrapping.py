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

import time
from datetime import datetime

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


# In[4]:


def keyword(word,no_news):
    
    """Because of the specific code to do BBC website, a function is implemented to, first, start the browser and open the bbc website for, after accepting the cookies and using the search bar placed in it to search the word introduced in the function with Selenium. Because of the use of a VPN, the cookies might not be required to accept, so, for this reason it's used a try and except method to avoid errors if, depending on the region of the VPN; on the other side, it's used a while loop which includes to get all the elements which tag is 'a' and attribute 'href', to get all the url links of the list of news; to be sure that it's downloaded just news it's a pplied an if method which has to include 'news' in the url and not 'help' or 'live'. Once it's got the proper url this one is saved in a list out of the loop and it's extracted the title, the content and the date split in day, month and year with Beautifulsoup and saved in a dictionary with key the name of the column and the value the content. During the while, it's also introduced another Selenium method with a try and except, so, if the condition is not met, which is the number of news required and introduced within the function call, it will try to click in 'next page' to continue downloading, if the number is not met and there's no more 'next page' tag, means that the website finished all the results and it didn't download all the content required, so, it's stopped the while to continue performing the dictionary and setting up the DF.
It's also to include in the description the use of selenium to scroll down on the website until finding the button 'next page' to continue downloading content."""
    
    url='https://www.bbc.com/news'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    try:
        cookies_accept = driver.find_element(By.CLASS_NAME, 'fc-button').click()
        cookies_2= driver.find_element(By.CLASS_NAME, 'banner-button').click()
    except:
        pass
    
    time.sleep(3)
    search_bar  = driver.find_element(By.LINK_TEXT, 'Search BBC').click()
    search_bar  = driver.find_element(By.ID, 'search-input')
    search_bar.send_keys(word)
    search_bar.send_keys(Keys.RETURN)
    
    link_lst=[]
    

    while len(link_lst)<no_news:
        lnks           = driver.find_elements(By.TAG_NAME,"a")
        lst_bbc        = [lnk.get_attribute('href') for lnk in lnks]
        lst_bbc_       = [url for url in lst_bbc if '/news/' in url and '/help' not in url and '/live/' not in url]
        
        try:
            more_button = driver.find_element(By.LINK_TEXT, 'next page')
            driver.execute_script("arguments[0].scrollIntoView();",more_button)
            more_button.click()
            
        except:
            break

        for i in lst_bbc_:
            link_lst.append(i)

        link_lst= list(set(link_lst))

        list_title=[]
        list_soup=[]
        for url in link_lst:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser")
            article=soup.getText().replace('\'', "´").strip()
            article = article[:article.find('More on this story')]
            title = soup.title.string
            list_soup.append(article)
            list_title.append(title)

        day_list=[]
        month_list=[]
        year_list=[]
        for url in link_lst:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            time_tag = soup.find('time')
            timestamp = time_tag['datetime']
            dt = datetime.fromisoformat(timestamp[:-1])
            date_str = dt.strftime("%d-%m-%Y")


            day, month, year = date_str.split('-')

            day_list.append(day)
            month_list.append(month)
            year_list.append(year)




    dict_bbc={'title': list_title,
            'article': list_soup,
             'link':link_lst,
             'day':day_list,
             'month': month_list,
             'year': year_list}
    df=pd.DataFrame(dict_bbc)
    driver.close()
    return df

