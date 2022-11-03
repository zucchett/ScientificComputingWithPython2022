#!/usr/bin/env python
# coding: utf-8

# In[3]:

#Computing the distance

import math

u = [0, 6]
v = [8, 0]
def euclideanDistance(u,v):
    return math.sqrt( ((u[0]-v[0])**2)+((u[1]-v[1])**2) )

euclideanDistance(u,v)


# In[ ]:




