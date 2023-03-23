#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql
import sqlalchemy as alch 
from getpass import getpass
import pandas as pd

import os
from dotenv import load_dotenv


# In[2]:


load_dotenv()


# # Getting the details to run the engine

# In[41]:


password = os.getenv("password")
username = os.getenv("user")
server   = os.getenv('server')
dbName   = os.getenv('dbName')
connectionData=f"mysql+pymysql://{username}:{password}@{server}/{dbName}"
engine   = alch.create_engine(connectionData)


# In[42]:


bbc_raw=pd.read_csv('data/raw/bbc_raw.csv')
cnn_raw=pd.read_csv('data/raw/cnn_raw.csv')
pdo_raw=pd.read_csv('data/raw/pd_raw.csv') 
rt_raw =pd.read_csv('data/raw/rt_raw.csv') 


# In[43]:


bbc_raw.to_sql('bbc', engine, if_exists='replace', index=False)
cnn_raw.to_sql('cnn', engine, if_exists='replace',index=False)
pdo_raw.to_sql('people',engine, if_exists='replace',index=False)
rt_raw.to_sql('RT',engine, if_exists='replace',index=False)


# ## query for 2023

# In[44]:


def query_2023(table,engine):
    df=pd.read_sql_query(f""" SELECT * FROM {table}
    WHERE year>2022""", engine)
    return df


# In[45]:


def to_sql(df, table, engine):
    df.to_sql(f'{table}', engine, if_exists='replace',index=True)
    return


# In[55]:


def drop_op_less_2023(table,engine):
    pd.read_sql_query(f"""DELETE FROM {table} WHERE title  like "^Opinion";
    SELECT * FROM {table};""",engine)
    return 

