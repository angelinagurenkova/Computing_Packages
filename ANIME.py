#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


# In[44]:


#1
import pandas as pd 
data = pd.read_csv('anime.csv') 
print(data)


# In[6]:


#2
data1 = data.head(10)
print(data1)


# In[34]:


#3
data['Episodes'] = data['Episodes'].replace('?', 'NaN')
data['Voters'] = data['Voters'].str.replace(",", "")
data = data.astype({'Episodes': 'float32',
                    'Title': 'string',
                    'Production': 'string',
                    'Source': 'string',
                    'Genre': 'string',
                    'Airdate': 'string',
                    'Voters': 'int32',
                    'Rating': 'float32',
                    'Theme': 'string'})
print(data.info())


# In[18]:


#4
data.rename(columns=dict(zip(data.columns, list(map(lambda x: x.lower().replace(' ', '_'), data.columns)))), inplace=True)


# In[19]:


#5
print(data.describe())


# In[21]:


#6
print(data.production.value_counts())
print(data.source.value_counts())
print(data.genre.value_counts())


# In[57]:


data.Genre = data.Genre.str.lower()
data.Genre = data.Genre.str.replace(' ', '_')
data.Genre = data.Genre.str.replace(',', ' ')

g_set = set()
for i in data.Genre.str.split():
    for gen in i:
        g_set.add(gen)

g_dct = dict()
r_dct = dict()
for i in g_set:
    g_dct[i] = 0 
    r_dct[i] = 0

for i in data.Genre.str.split():
    for gen in i:
        g_dct[gen] += 1
print(g_dct)

for i in range(0,989):
    for gen in data.iloc[i].Genre.split():
        r_dct[gen] += data.iloc[i].Rating

for key in r_dct.keys():
    r_dct[key] = r_dct[key] / g_dct[key]
print(r_dct)
        
plt.rcParams["font.size"] = '7'
fig, ax = plt.subplots(2, 1)
fig = plt.figure("anime")

ax[0].bar(g_dct.keys(), g_dct.values())
ax[0].set_title("Genre")

ax[1].bar(r_dct.keys(), r_dct.values())
ax[1].set_title("Rating")

plt.show()


# In[ ]:




