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
st.write('-History:')
st.write('')
st.write(', Geopolitics, journalism ')
st.write('## Newspapers analysed')
st.write('### BBC:')
st.write('- Hisotry, background of subjetivity')

image_1 = Image.open('pics/wordcloud_uk.png')
st.image(image_1, caption='wordcloud shaped with the union jack')


st.write('### CNN:')
st.write('- Hisotry, background of subjetivity')

image_2 = Image.open('pics/wordcloud_usa.png')
st.image(image_2, caption='wordcloud shaped with the capitol')


st.write("### People's Daily Online:")
st.write('- Hisotry, background of subjetivity')

image_3 = Image.open('pics/wordcloud_china.png')
st.image(image_3, caption='wordcloud shaped with Xi Jinping, actual president PRC')

st.write("### People's Daily Online:")
st.write('- Hisotry, background of subjetivity')

image_4 = Image.open('pics/wordcloud_russia.png')
st.image(image_4, caption="wordcloud shaped with Saint Basil's Cathedral, Red Square, Moscow")

st.write('## Findings:')
st.write("#### Subjetivity: As it's shown in the graph no.")
st.write('#### Polarity: ')
st.write('#### Number of publications by newspaper:')
st.write('#### Recurrent topics:')
st.write('#### Most used words, difference in between the "two blocks":')
st.write('#### Overall of words ')

st.write('## Conclusions:')

st.write('## Disclamer:')
st.write('This project is being done with specific libraries and an adaptation of a MIT nomenclator, which, in between the availables, are the most reliable. Due to these reasons, the accuracy obtained can be as not precise as the reality; the fact of taking the words out of their context might infer in not accurate conclusions caused by the loss of meaning of the overall article.')