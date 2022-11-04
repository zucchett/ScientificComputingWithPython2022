#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Machine precision

delta = 1
z=0
while delta > 1e-20:
    if 1 + delta == 1:
        print('1 +', delta, "  = 1")
        flag = delta/0.1
        break
    else:
        print('1 +', delta, "  != 1")
    z+=1
    delta=delta*0.1
print("The machine precision for floating point numbers is up to ", z, "th digit after the point.")


# In[ ]:




