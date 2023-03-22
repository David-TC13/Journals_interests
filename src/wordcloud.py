#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# In[3]:

def wordcloud(df,file):
    """This function creates a wordcloud of a specific DF and with a specific shape"""
    words=[word for txt in df['word'] for word in txt]
    text = ' '.join(words)
    mask = np.array(Image.open(f"pics/{file}"))
    wordcloud = WordCloud(width=1000, height=800, background_color='black',mask=mask,contour_width=1, contour_color='gray').generate(text)
    plt.figure(figsize=(8,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(f'pics/wordcloud_{file}', dpi=300, bbox_inches='tight')
    return plt.show()

# In[ ]:
