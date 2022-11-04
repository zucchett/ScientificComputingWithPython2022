#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Global variables

x = 5

def f(alist):
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)
print("alist has NOT been changed")

