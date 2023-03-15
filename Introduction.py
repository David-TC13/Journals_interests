#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title('Is any geopolitical influence on the press we read around the globe?')

image = Image.open('pics/wordcloud_press.png')
st.image(image, caption='wordcloud shaped as reporter')

st.write('## Introduction')
st.write('In a globalised world, has to be ')
