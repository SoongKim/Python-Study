#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import bs4, requests


# In[2]:


targetUrl = "https://www.kopo.ac.kr/kangseo/content.do?menu=262"

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
resp = requests.get(targetUrl,headers = {'User-Agent':user_agent} )

targetText = resp.text


# In[3]:


targetText


# In[4]:


targetObj = bs4.BeautifulSoup(targetText, "html.parser")


# In[5]:


targetObj


# In[6]:


eachrow = targetObj.findAll(name = "td")


# In[7]:


mealTags = []


# In[8]:


for i in range(0, len(eachrow)):
    mealTag = eachrow[i].text
    mealTags.append(mealTag)


# In[9]:


mealList = []


# In[10]:


for j in range(0, len(mealTags)):
    mealTags[j] = mealTags[j].replace("\r", "").replace("\n", "")
    mealList.append(mealTags[j])


# In[11]:


mealInfo = mealTags[0::2]


# In[12]:


mealInfo


# In[13]:


mealInf0 = mealInfo[:10]


# In[14]:


mealInf0


# In[15]:


weekList = []


# In[16]:


menuList = []


# In[17]:


for d in range(0, len(mealInf0)):
    if(d % 2 == 0):
        weekList.append(mealInf0[d])
    else:
        menuList.append(mealInf0[d])


# In[18]:


menuDf = pd.DataFrame(menuList, weekList)


# In[19]:


menuDf.columns = ["강서폴리텍_스마트금융학과"]


# In[20]:


menuDf


# In[21]:


menuDf.to_csv("./menu.csv", encoding = "ms949")


# In[21]:


menuDf.to_csv("./menuUTF.csv", encoding = "UTF-8")