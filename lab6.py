#!/usr/bin/env python
# coding: utf-8

# In[5]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[10]:


d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  
 


# In[11]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[12]:


#Intersection
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)


# In[13]:


#Union
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx | sety
print(seta)


# In[14]:


setp = set(["Red", "Green"])
setq = setp.copy()
print(setq)
setq.clear()
print(setq)


# In[15]:


setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)
issubset = setz <= sety
print(issubset)
issuperset = sety >= setz
print(issuperset)


# In[16]:


setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)
#Set difference
setb = setx - setz
print(setb)


# In[17]:


setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
#Symmetric difference
setc = setx ^ sety
print(setc)


# In[ ]:




