#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pymysql
import sqlalchemy as alch 
from getpass import getpass
import pandas as pd

import os
from dotenv import load_dotenv

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image

load_dotenv()

password = os.getenv("password")
username = os.getenv("user")
server   = os.getenv('server')
dbName   = os.getenv('dbName')
connectionData=f"mysql+pymysql://{username}:{password}@{server}/{dbName}"
engine   = alch.create_engine(connectionData)

st.set_page_config(
     page_title='Press influences',
     
     layout='wide',
)


st.title('Filtering news, what do you want to read today?')

df_bbc=pd.read_sql_query(f""" SELECT * FROM bbc""", engine)
df_cnn=pd.read_sql_query(f""" SELECT * FROM cnn""", engine)
df_pd= pd.read_sql_query(f""" SELECT * FROM people""", engine)
df_rt=pd.read_sql_query(f""" SELECT * FROM RT""", engine)



df = pd.concat([df_bbc,df_cnn,df_pd,df_rt])


year = st.selectbox('Year', sorted(df['year'].unique()))
df2 = df[(df['year'] == year)]

month = st.selectbox(' Month', sorted(df2['month'].unique()))

df3= df2[(df2['month'] == month)]
day=st.selectbox('Day',sorted(df3['day'].unique()))

df4=df3[(df3['day'] == day)]

title= st.selectbox('Title', df4['title'])
df5= df4[df4['title']==title]

link=df5['link'].values[0]

st.write(df5.loc[:,['subjectivity','polarity','word','source','topic']])

if st.button("Read full article"):
    js = "window.open('{}')".format(link)
    components.html('<script>{}</script>'.format(js))