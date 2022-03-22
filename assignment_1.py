#!/usr/bin/env python
# coding: utf-8

# In[51]:


import os
import numpy as np


# In[52]:


####question 1
def sample(a,b):
    return(a+b)


# In[53]:


sample(5,7)


# In[5]:


###question 2
a=3
b=str


# In[56]:


a+b


# In[57]:


del(input)


# In[7]:


####question 3
c='Data Science'
if 'S' in c:
    print("true")
else:
    print("false")


# In[98]:


#####question 4
def sam():
    d=list(input("enter the value"))
    f=len(d)
    print(f)
    if d[0]==d[f-1] :
        print("the first and last number is equal")
    else:
        print("The number is different")
        
        
    


# In[99]:


sam()


# In[123]:


#####question 5
def prnt():
    j=[]
    k=int(input("enter the length"))
    for i in range(0,k):
        a=int(input("enter the value"))
        j.append(a)
        print(j[i]%5)
        if j[i]%5 == 0:
            print(j[i]," : The number is divisible")
        else:
            print(j[i]," : The number is not divisible")


# In[124]:


prnt()


# In[125]:


####question 6
def calc(a,b):
    return(a+b,a*b)


# In[126]:


calc(2,5)


# In[127]:


###question 7
def erro(a=b,c):
    print("the dec is correct")


# In[128]:


def erro(c,a=b):
    print("the dec is correct")


# In[130]:


erro(c)


# In[148]:


####question 8
def addex(a):
    if len(a)==0:
        return 0
    else:
        return a[0] + addex(a[1:]) 


# In[ ]:





# In[150]:


print(addex([0,1,2,3,4,5,6,7,8,9]))


# In[169]:


#####question 9
a=[12,11,53,22,21,77,87,88,98]
x_odd=list(filter(lambda y: y%2 !=0,a))
print(x_odd)
sqre=lambda x:x*x
for i in range(0,len(x_odd)):
    print(sqre(x_odd[i]))


# In[172]:


######question 10
number = [1,2,3,4,5,6]
sqre=map(lambda x : x*x ,number)
print(list(sqre))


# In[ ]:




