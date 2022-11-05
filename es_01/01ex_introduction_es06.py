# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:40:46 2022

@author: Federico
"""

#declare the first variable and its type
print("Data type 1? (int, float, str)")
type1=input()
print("Value 1?")
value1=input()
if type1=="int":
    x1=int(value1)
elif type1=="float":
    x1=float(value1)
elif type1=="str":
    x1=value1
else: print("Error on v1")

#declare the second variable and its type
print("Data type 2? (int, float, str)")
type2=input()
print("Value 2?")
value2=input()
if type2=="int":
    x2=int(value2)
elif type2=="float":
    x2=float(value2)
elif type2=="str":
    x2=value2
else: print("Error on v2")
    
#calculate the sum, if possible, and print it    
try:
    result=x1+x2
    print("The sum of the two variables is: ",result)
except:
    print("A problem occurred")