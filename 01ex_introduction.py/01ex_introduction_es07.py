#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Cubes

#a)

cubes = []
start = int(input("enter a value: "))
end = int(input("enter the end value: "))

for x in range(0,10):
    
   cubes.append(x**3)
print(str(cubes))

#b)

cubes = [i**3 for i in range(0, 11)]
print(cubes)


# In[ ]:




