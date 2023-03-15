#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
     page_title='Press influences',
     
     layout='wide',
)


st.title('Filtering news, what do you want to read today?')


df=pd.read_csv('data/dfcomplete.csv')

year = st.selectbox('year', df['year'].unique())
month = st.selectbox('month', df['month'].unique())
day = st.selectbox('day', df['day'].unique())
df2 = df[(df['year'] == year) & (df['month'] == month) & (df['day'] == day) ]
title= st.selectbox('Title', df2['title'])
df3= df2[df2['title']==title]

st.write(df3.loc[:,['article','source','topic','subjetivity','polarity','word','link']])
