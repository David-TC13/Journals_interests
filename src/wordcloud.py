#!/usr/bin/env python
# coding: utf-8

# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


df_bbc_russia=pd.read_csv('data/processed/bbc_russia_proc.csv')
df_bbc_china=pd.read_csv('data/processed/bbc_china_proc.csv')
df_cnn_russia=pd.read_csv('data/processed/cnn_russia_proc.csv')
df_cnn_china=pd.read_csv('data/processed/cnn_china_proc.csv')
pdo_uk=pd.read_csv('data/processed/pdo_united_kingdom_proc.csv')
pdo_usa=pd.read_csv('data/processed/pdo_united_states_proc.csv')
rt_uk=pd.read_csv('data/processed/rt_united_kingdom_proc.csv')
rt_usa=pd.read_csv('data/processed/rt_united_states_proc.csv')


# In[4]:


def wordcloud(df):
    words=[word for txt in df['word'] for word in txt]
    text = ' '.join(words)
    wordcloud = WordCloud(width=1000, height=800, background_color='white').generate(text)
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt.show()

# In[5]:





# In[ ]:




