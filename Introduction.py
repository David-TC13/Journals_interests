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
st.write('''After the second world war, the world ended up split into two main blocs; after falling the "Nazi Empire", the world was divided by the Allies in two blocs:
         on one side, the Western bloc which included USA, UK , and, on the other side the Eastern bloc which included most of the communist countries at the time.
         ''')
st.write('''Just after this division,particulary noted in the city of Berlin, the tensions were raised in between both blocs; the creation of the NATO as a containment for 
the Soviet influence is considered the starting point of what was called the Cold War; as counterpart, the URSS created the Warsaw Pact in order the maintain the status quo. 
 ''')

st.write('''Cold war was used to determine a period of history where, USA and URSS had an increasing geopolitical tension relationship without a straight confrontation, 
using nuclear arsenal development and conventional military deployment, psychological warfare, propaganda campaigns, espionage, far-reaching embargoes, rivalry at sports events, 
and technological competitions such as the Space Race.
 ''')

st.write("""On this atmosphere, became crucial how the messages are said, how to spread widely, and, most important thing, what is the purpose of it. For this reason, the press 
became a key point as a powerful tool as psychological warfare and propaganda campaigns. As 'Argumentum Ad Verecundiam' press has a relevant position in society, so, it's assumed 
what's pubblished it's true.
""")

st.write("""Ultimately, this relevance is the cause of the governments and private institutions interest to influence on what they publish or what to ommit. One recent example can be seen
        during the russian invasion of Ukraine, which, it was considered by the European Union russian press like RT or Sputnik agencies for misinforming the population and, for this reason
        they were banned to broadcast in Europe. As and immediate consequence of this decision brought this project to a extra scope, which was to find the way to get the information from 
        this broadcast agency (RT) and evaluate if that was true, standarising some parameters and comparing them between the Western broadcast agencies, as well. For this reason, one of the main challenges has been to managed to 'bypass' this prohibition, trying to find a proper tool 
        to reach it, by using a VPN based on Japan.""")         

st.write('## Newspapers analysed')
st.write('### BBC:')
st.write('- Hisotry, background of subjetivity')

image_1 = Image.open('pics/wordcloud_uk.png')
st.image(image_1, caption='wordcloud with BBC logo')


st.write('### CNN:')
st.write('- Hisotry, background of subjetivity')

image_2 = Image.open('pics/wordcloud_usa.png')
st.image(image_2, caption='wordcloud shaped with CNN logo')


st.write("### People's Daily Online:")
st.write('- Hisotry, background of subjetivity')

image_3 = Image.open('pics/wordcloud_china.png')
st.image(image_3, caption="wordcloud shaped People's Daily Online logo")

st.write("### RT:")
st.write('- Hisotry, background of subjetivity')

image_4 = Image.open('pics/wordcloud_russia.png')
st.image(image_4, caption="wordcloud shaped RT logo")

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