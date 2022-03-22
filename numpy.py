#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[8]:


####question1
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)


# In[10]:


arr1.shape


# In[12]:


arr1.ndim


# In[ ]:


###question2


# In[23]:


arr2=np.arange(0,21)
print(arr2[slice(0,21,5)])


# In[24]:


###question3


# In[34]:


arr3=np.array([[1,2,3,4,5],[8,9,10,11,12],[12,13,14,15,16],[1,2,3,4,4],[0,9,8,7,6],[0,9,6,5,4],[5,3,2,1,0]])
print(arr3)
arr3.shape


# In[39]:


arr4=np.array([[0,1,2,3,4],[4,5,6,7,8],[1,2,3,4,5],[5,6,7,8,9],[0,1,2,3,4],[4,5,6,7,8],[4,7,8,9,10]])
print(arr4)
arr4.shape


# In[41]:


###addition
arr5=arr3+arr4
arr5


# In[42]:


###subtraction
arr6=arr3-arr4
arr6


# In[43]:


####multiplication
arr7=arr3*arr4
arr7


# In[44]:


arr8=arr3/arr4
arr8


# In[48]:


###question 4

arr9=np.array([[1,2],[3,4]])
arr10=np.array([[4,9,0],[6,7,10]])
arr11=arr9*arr10
arr11


# In[50]:


#####question 5

arr12=([[1,2],[3,4]])
arr13=([[4,5],[5,6]])
np.vstack([arr12,arr13])


# In[51]:


np.hstack([arr12,arr13])


# In[ ]:


#######question 6


# In[56]:


np.append(arr12,arr13,axis=0)


# In[57]:


np.append(arr12,arr13,axis=1)


# In[60]:


###question 7
list1=[[1,2,3,5],[7,8,9,10]]
df1=pd.DataFrame(list1)
print(df1)


# In[62]:


df1.rename(columns={0 : "num1", 1 : "num2",2:"num3",3:"num4"})


# In[5]:


###question 8

dict1={'name' : ['ab','bc','cd','ef'] , 'age' : [20,30,40,50], 'ordr_no' : [1,2,3,4],
       'loc' : ['us','thlnd','chn','ukraine'],'hse_no' : [1,2,3,4],'lap_no':[3,6,7,9],
       'class_no' :[7,8,9,12],'sub_nm':['IT','CSE','ECE','EEE']}


# In[6]:


df2=pd.DataFrame(dict1)
df2.shape
df2


# In[81]:


######question 9
df2.iloc[3]


# In[34]:


df2.loc[df2['name'] == 'ef']


# In[35]:


###question 10
df2.isnull()


# In[26]:


#####question 11
dict2={'age' : [100,200,None,200,400], 'std' : [1,2,3,4,5]}
df3=pd.DataFrame(dict2)
df3


# In[33]:


df3.fillna(100)


# In[48]:


get_ipython().run_line_magic('pinfo', 'df3.dropna')


# In[54]:


######question 12
dict3={'age' : [100,200,None,200,400], 'std' : [1,2,None,4,5]}
df4=pd.DataFrame(dict3)
df4.dropna(axis=0)


# In[56]:


dict4={'Age' : [25,30,45,35,33,35,25,52,21,24,48,22,27,28,21,51,23] , 'Hair Color' : ['Black','Blacka','Red','Blond','Brown','Brown','Black','Brown','Blond','Blond','Black','Black','Brown','Black','Blond','Black','Brown'], 'U.S.Region' : ['Southwest','Northwest','Northeast','Southwest','Southwest','Northeast','Southwest','Southeast','Southwest','Northeast','Southwest','Southwest','Northeast','Southeast','Southeast','Northwest','Southeast'], 'Validation' : [1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1]}


# In[58]:


df5=pd.DataFrame(dict4)
df5


# In[68]:


#####question 13
df5.groupby(['U.S.Region']).mean(['Age'])


# In[71]:


df6=df5.groupby(['Hair Color']).sum()
df6


# In[73]:


df6.reset_index()


# In[74]:


df5.groupby(['U.S.Region']).mean()


# In[75]:


df5.groupby(['U.S.Region']).median()


# In[86]:


####question 14
df7=df5.iloc[[0,1,2,3,4,5,6,7]]
df7


# In[89]:


df8=df5.iloc[[8,9,10,11,12,13,14,15,16]]
df8


# In[98]:


df9=pd.merge(df7,df8,how='inner',on='Hair Color')
df9


# In[99]:


df10=pd.merge(df7,df8,how='left',on='Hair Color')
df10


# In[100]:


df11=pd.merge(df7,df8,how='right',on='Hair Color')
df11


# In[102]:


####question 15
pd.concat([df7,df8])


# In[104]:





# In[ ]:




