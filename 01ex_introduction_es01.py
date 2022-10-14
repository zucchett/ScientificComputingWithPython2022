# -*- coding: utf-8 -*-
"""
U Berk Cakmakci

"""

list_a = []
for i in range(1, 101, 1):
    if i%15 == 0:
        y="HelloWorld"
        #print(y)
    elif i%5 == 0:
        y="World"
        #print(y)
    elif i%3 == 0:
        y="Hello"
       # print(y)
    else:
        y=i
        #print(i)
        
    list_a.append(y)
    
print(list_a)

list_b = str(list_a)
list_b = list_b.replace('Hello', 'Python')
list_b = list_b.replace('World', 'Works')
print(list_b)
