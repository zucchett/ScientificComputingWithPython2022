#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#The HelloWorld replacement

def Hello_World(num):
    
     if num%3==0 and num%5==0:
        return 'HelloWorld'
    
     elif num %3 ==0:
        return 'Hello'

     elif num % 5==0:
        return 'World'
     else:
        return num

for n in range(1,101):
    print(Hello_World(n)) 

