#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title('Filtering news, what do you want to read today?')
st.write("Welcome to Streamlit! 👋")
df=pd.read_csv('data/dfcomplete.csv')
st.dataframe(df)