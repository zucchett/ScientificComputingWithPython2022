#!/usr/bin/env python
# coding: utf-8

# In[2]:


#The Fibonacci sequence (part 2)

def recur_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
fibo_list = []
print("Fibonacci sequence:")
for i in range(20):
    fibo_list.append(recur_fibo(i))

print(fibo_list)


# In[ ]:




