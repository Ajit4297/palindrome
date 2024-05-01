#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=(input())
i=0
j=len(n)-1
flag=True


while i<j:
    if n[i]!=n[j]:
        flag=False
        break
    i=i+1
    j=j-1
if flag==True:
    print('true')
else:
    print('false')


# In[ ]:




