#!/usr/bin/env python
# coding: utf-8

# In[6]:

#Nested list comprehension

print([(a, b, c) for a in range(1, 101) for b in range(a, 101)
       for c in range(b, 101) if a**2 + b**2 == c**2])

# In[ ]:




