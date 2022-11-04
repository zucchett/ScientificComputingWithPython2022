#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Decorators

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)    
    return wrapper

@hello
def square(x):
    return x*x

print(square(5))


# In[ ]:




