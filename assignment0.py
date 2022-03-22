#!/usr/bin/env python
# coding: utf-8

# In[23]:


####question1
import os
import numpy as np


# In[2]:


os.getcwd()


# In[4]:


os.chdir('/users/automation/Downloads')


# In[10]:


####question2

x=2
print(type(x))


# In[11]:


del x


# In[12]:


x=2.2
print(type(x))


# In[13]:


del x


# In[14]:


x='str'
print(type(x))


# In[15]:


del x


# In[16]:


#####question 3


# In[18]:


for ='fgh'


# In[19]:


####question 4


# In[21]:


a="""My name is Deepika.
I am in Python Training"""
print(a)


# In[25]:


#####question 5
b=np.arange(100,999,8)
print(b)


# In[29]:


#####question6
c=np.arange(1,10,1)
d=[]
for i in c:
    d.append(i)
    print(d)
    if i/2 in d:
        break
    else :
        print("looop will continue")
    


# In[32]:


####question 7
def docstr():
    '''this is a sample of docstring'''
    return None


# In[34]:


print(docstr.__doc__)


# In[35]:


####question 9


# In[38]:


os.chdir('/users/automation/')


# In[44]:


f=np.arange(0,100,1)
lst1= [ i for i in f if i%2==1 ]
print(lst1)


# In[45]:


####question 10
s='Deepika'
lst2 = [i for i in s if i not in ('a','e','i','o','u')]
print(lst2)


# In[ ]:




