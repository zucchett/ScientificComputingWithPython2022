# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:46:39 2022

@author: gozde
"""

#a

for x in range(1, 101):
    if x%15 == 0: 
       print ("Hello World") 
       

    elif x%3 == 0:
           print ("Hello")
           
           
    elif x%5 == 0:
           print ("World")
        
    else:
        print (x) 


#b

result = []

for x in range(1, 101):
    if x%3 == 0 and x%5 ==0:
       x = "Hello World"
       print (x) 
       result.append(x)
       
    elif x%3 == 0:
        x = "Hello"
        print (x)
        result.append(x)
           
    elif x%5 == 0:
        x = "World"
        print(x)
        result.append(x)
          
    else:
        print (x)
        result.append(x)
        
y = tuple(result)
print(y)


result = list(y)

for x in range(len(result)):
    if result[x] == "Hello":
        result[x] = "Python"

    if result[x] == "World":
        result[x] = "Works"

z = tuple(result)
print(z)
