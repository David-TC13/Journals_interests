#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np


st.title('Is any geopolitical influence on the press we read around the globe?')

df=pd.read_csv('data/dfcomplete.csv')
st.dataframe(df)