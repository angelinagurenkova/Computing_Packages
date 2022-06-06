#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[2]:


import pandas as pd
data = pd.read_csv('titanic.csv') 
print(data)


# In[3]:


print(data.head(10))


# In[8]:


import matplotlib.pyplot as plt
plt.title("Количество выживших:")
data['Survived'].value_counts().plot(kind='pie', autopct='%1.0f%%')
plt.show()

plt.title("Выжившие в зависимости от класса и пола")
data.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True).sort_values().plot(kind='bar')
plt.show()


# In[9]:


sum18_1 = data[data['Age'] < 18][data['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum55_1 = data[data['Age'] < 55][data['Age'] >= 18][data['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum100_1 = data[data['Age'] >= 55][data['Survived'] == 1].groupby(["Age"])["Survived"].value_counts().sum()
sum18_0 = data[data['Age'] < 18][data['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
sum55_0 = data[data['Age'] < 55][data['Age'] >= 18][data['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
sum100_0 = data[data['Age'] >= 55][data['Survived'] == 0].groupby(["Age"])["Survived"].value_counts().sum()
pd.DataFrame([sum18_1/891, sum55_1/891, sum100_1/891 ,sum18_0/891, sum55_0/891, sum100_0/891],
             columns=['Количество выживших'],
             index=['Выжившие < 18', 'Выжившие < 55', 'Выжившие >= 55', 'Погибшие < 18', 'Погибшие < 55', 'Погибшие >= 55' ])\
    .sort_values('Количество выживших').plot(kind='bar', title='Выжившие в зависимости от возраста')
plt.show()


# In[10]:


print(data["Age"].head(5), end="\n------\n")

print(data[["Age", "Sex"]].head(5), end="\n------\n")
data["Realtives"] = data["SibSp"] + data["Parch"] 
print(len(data[~data["Realtives"].isin([0])]), end="\n------\n")
print(len(data[data["Embarked"].isin(["S"])]), end="\n------\n")
surv = len(data[data["Survived"].isin([1])])
not_surv = len(data[data["Survived"].isin([0])])
print(f"Survived: {surv}", end="\n------\n")
print(f"Not survived: {not_surv}", end="\n------\n")

dct = {1 : "Elite", 2 : "Middle", 3 : "Prol"}

data = data.replace({"Pclass" : dct})

data["Fare_bin"] = "Expensive"
data.loc[(data.Fare < 20), "Fare_bin"] = "Cheap"

data = data.dropna()
data = data.reset_index()

print(data)


# In[ ]:




