#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##question 1


# In[11]:


def test_fun():
    age=int(input("enter the age"))
    name=str(input("enter the name"))
    print("Hi ",name, "you will turn to 100 after ", 100-age ,"years")


# In[12]:


test_fun()


# In[ ]:


###question 2


# In[13]:


import pandas as pd


# In[16]:


####pd.DataFrame.groupby used to do some calculation on the dataframe.This group by function is used to combine the values


# In[60]:


dict1={'Name' : ['a','b','c'] , 'Mark' : [100,20,30]}


# In[77]:


df1=pd.DataFrame(dict1)
df1


# In[24]:


get_ipython().run_line_magic('pinfo', 'pd.DataFrame.groupby')


# In[27]:


df1.groupby(['Mark']).sum()


# In[28]:


###question 3


# In[35]:


list1=[(1,2,3,4,5),(7,8,9,10,11)]


# In[36]:


df2=pd.DataFrame(list1)
df2


# In[37]:


###question 4


# In[39]:


list2=[(1,2,3,4,5),(6,8,9,10,11)]
df3=pd.DataFrame(list2)
df3


# In[41]:


list3=[('a','b','c','d','e'),(2,3,4,5,6)]
df4=pd.DataFrame(list3)
df4


# In[43]:


df5=df3.append(df4)
df5


# In[50]:


df6=[df3,df4]
df6=pd.concat(df6)
df6


# In[57]:


get_ipython().run_line_magic('pinfo', 'pd.merge')


# In[64]:


dict2={'Name' : ['a','c','d'], 'Mark' : [10,20,30]}
df6=pd.DataFrame(dict2)
df6


# In[65]:


df6.merge(df1,left_on='Name',right_on='Name')


# In[ ]:


####question 5


# In[67]:


c=(1,2,3)
type(c)
e=[1,2,3]
type(e)


# In[68]:


#####the values of the object in list  can be modified,but the values of the object in tuple is immutable.


# In[69]:


######question 6


# In[70]:


import numpy as np


# In[72]:


array1=np.array([1,5,3,100,4,48])
array1


# In[73]:


array1.mean()


# In[74]:


array1.std()


# In[79]:


n = len(array1)
array1.sort()
  
if n % 2 == 0:
    median1 = array1[n//2]
    median2 = array1[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = array1[n//2]
print("Median is: " + str(median))


# In[80]:


######question 7
list2=[1,1,2,3,4,5,6]
list2


# In[83]:


res=[]
for i in list2:
    if i not in res:
        res.append(i)
    print(res)
    


# In[85]:


######question 8
def mult(n):
    return n*n

lst=[1,2,3,4,5]
op = map(mult,lst)
print(list(op))

####using map() the function can be applied on every object of the list or tuple


# In[87]:


######question 9
a=10
b=20
if (a<b):
    pass
else:
    print(a)
    
######pass function will iterprutted by compiler ......and it will be used to check the 


# In[91]:


######question 10
d=[1,2,3,4]
e=['a','b','c','d']
c=np.vstack((d,e))
print(c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




