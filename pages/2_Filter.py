#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from getpass import getpass
import pandas as pd



import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(
     page_title='Press influences',
     
     layout='wide',
)


st.title('Filtering news, what do you want to read today?')
df=pd.read_csv('data/df_together.csv')

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