#!/usr/bin/env python
# coding: utf-8

# In[21]:


import bs4, requests


# In[22]:


targetUrl = ("https://sparkkorea.com/%ed%80%b4%ec%a6%88/")


# In[23]:


try:
    resp = requests.get(targetUrl)
except Exception as e:
    print(e)


# In[24]:


resp


# In[25]:


webPageSrc = resp.text


# In[27]:


targetObj = bs4.BeautifulSoup(webPageSrc, "html.parser")


# In[28]:


targetObj


# In[45]:


targetTag = targetObj.find(name = "div", attrs = {"id":"id_spark_quiz"})


# In[46]:


targetTag


# In[47]:


aTags = targetTag.findAll(name = "a")


# In[49]:


lenAtags = len(aTags)


# In[50]:


for i in range(0, lenAtags):
    print(aTags[i].attrs["href"])


# In[51]:


nameList = []


# In[52]:


linkList = []


# In[53]:


for i in range(0, lenAtags):
    quizName = aTags[i].text
    quizLink = aTags[i].attrs["href"]
    
    nameList.append(quizName)
    linkList.append(quizLink)


# In[54]:


nameList


# In[56]:


linkList


# In[57]:


import pandas as pd


# In[58]:


df01 = pd.DataFrame(zip(nameList, linkList))


# In[59]:


newColumns = ["이름", "퀴즈"]


# In[60]:


df01.columns = newColumns


# In[61]:


df01


# In[63]:


df01.to_csv("./noname.csv", encoding = "ms949")

