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


import requests
from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
import numpy as np



# In[4]:


def keyword(word, no_news):
    
    """Because of the specific code to do people's daily online website, a function is implemented to, first, start the browser and open their website for, after accepting the cookies and using the search bar placed in it to search the word introduced in the function with Selenium. Because of the use of a VPN, the cookies might not be required to accept, so, for this reason it's used a try and except method to avoid errors, depending on the region of the VPN; on the other side, it's used a while loop which includes to get all the elements which tag is 'a' and attribute 'href', to get all the url links of the list of news; to be sure that it's downloaded just news it's applied an if method which has to include '/2023'or '/2022' in the url. Once it's got the proper url this one is saved in a list out of the loop and it's extracted the title, the content(cleaned of specialk characters) and the date split in day, month and year with Beautifulsoup and saved in a dictionary with key the name of the column and the value the content. During the while, it's also introduced another Selenium method with a try and except, so, if the condition is not met, which can be a news without a proper date format, there's no 'more' button (which means the search in the website finished), or, the length of the list of news is not reach, pass."""
    
    url= 'http://en.people.cn'
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(3)
    try:
        cookies_button_deny  = driver.find_element(By.CLASS_NAME,'tipsClose').click()
    except:
        pass
    
    form = driver.find_element(By.NAME,"searchFormForPC")
    keyword_input = form.find_element(By.NAME,"keyword")
    keyword_input.send_keys(word)
    keyword_input.send_keys(Keys.RETURN)
    driver.close()
    
    driver.switch_to.window( driver.window_handles[0])
    
    link_lst=[]
    try:
    
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


            next_button = driver.find_element(By.LINK_TEXT, 'Next').click()

        
        dict_pc={'title': list_title,
             'article':list_soup,
             'link': link_lst,
             'day':day_list,
             'month':month_list,
             'year':year_list
                }
        df_cn= pd.DataFrame(dict_pc)
        df_cn.drop_duplicates(inplate=True)
        driver.close()
   
        return df_cn
    except:
        pass

