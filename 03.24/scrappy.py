#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


import bs4, requests


# In[21]:


mainUrl = "https://sparkkorea.com/%ed%80%b4%ec%a6%88/"


# In[22]:


try:
    resp = requests.get(mainUrl)
except exception as e:
    print(e)


# In[23]:


webPageSrc = resp.text


# In[24]:


htmlObj = bs4.BeautifulSoup(webPageSrc, "html.parser")


# In[14]:


htmlObj


# In[25]:


divs = htmlObj.findAll(name = "div")


# In[26]:


aTags = htmlObj.findAll("a")


# In[27]:


linkList = []


# In[32]:


for i in range(0, len(aTags)):
    try:
        linkList.append(aTags[i].attrs["href"])
    except Exception as e:
        print(e)


# In[34]:


targetTag = htmlObj.find(name = "div", attrs = {"id":"id_spark_quiz"})


# In[35]:


targetTag


# In[36]:


aLinks = targetTag.findAll(name = "a")


# In[37]:


quizList = []


# In[38]:


linkList = []


# In[41]:


for i in range(0, len(aLinks)):
    quizName = aLinks[i].text
    linkName = aLinks[i].attrs["href"]
    quizList.append(quizName)
    linkList.append(linkName)


# In[50]:


resultDf = pd.DataFrame(zip (quizList, linkList), columns = (["퀴즈 이름", "퀴즈 링크"]))


# In[81]:


resultDf.to_csv("./result.csv", encoding="ms949")

