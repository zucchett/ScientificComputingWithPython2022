#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nested functions

def square(num):
    return num*num

def cube(num):
    return num*num*num

sixth_power = (lambda num : cube(square(num)))

print(sixth_power(6))


# In[ ]:




