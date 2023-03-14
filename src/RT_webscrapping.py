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

    """Because of the specific code to do CNN website, a function is implemented to, first, start the browser and open the cnn website for, after accepting the cookies and using the search bar placed in it to search the word introduced in the function with Selenium. Because of the use of a VPN, the cookies might not be required to accept, so, for this reason it's used a try and except method to avoid errors, depending on the region of the VPN; on the other side, it's used a while loop which includes to get all the elements which tag is 'a' and attribute 'href', to get all the url links of the list of news; to be sure that it's downloaded just news it's applied an if method which has to include 'https://www.cnn.com/202' in the url. Once it's got the proper url this one is saved in a list out of the loop and it's extracted the title, the content and the date split in day, month and year with Beautifulsoup and saved in a dictionary with key the name of the column and the value the content. During the while, it's also introduced another Selenium method with a try and except, so, if the condition is not met, which can be a news without a proper date format, there's no 'more' button (which means the search in the website finished), or, the length of the list of news is not reach, pass.It's also to include in the description the use of selenium to scroll down on the website until finding the button 'more' to continue downloading content."""
    

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
                'day': day_list,
                'month': month_list,
                'year' : year_list
                }
        df= pd.DataFrame(dict_)
        month_map = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12 }
        df['month'] = df['month'].map(month_map)
        driver.close()
        return df
    
    except:
        pass

