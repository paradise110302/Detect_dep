#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pds


# In[2]:


import nltk


# In[11]:


nltk.download()


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import string


# In[5]:


from nltk.corpus import stopwords


# In[7]:


from nltk.tokenize import RegexpTokenizer


# In[9]:


from nltk.stem import WordNetLemmatizer


# In[10]:


from nltk.stem.porter import PorterStemmer


# In[14]:


import numpy as np


# In[14]:


dataset = pds.read_csv('Depression_Reddit_Database_Filtered.csv')


# In[15]:


dataset.shape


# # Removing HTML

# .

# In[9]:


def remove_html (text):
    soup= BeautifulSoup ( text,'lxml')
    html_free=soup.get_text()
    return html_free


# # Removing Punctuations

# In[12]:


def remove_punctuation (text) :
    no_punct ="".join([c for c in text if c not in string.punctuation])
    return no_punct


# # Instantiate Tokenizer

# In[13]:


tokenizer = RegexpTokenizer ( r\'w')


# In[ ]:




