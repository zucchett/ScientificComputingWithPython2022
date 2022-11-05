# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:36:05 2022

@author: Federico
"""

#sulle stringhe date
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
print("s1:", s1, "s2:",s2)
x=input("select the string (s1 or s2)\n")
scelta=0
if x=="s1": scelta=s1
elif x=="s2": scelta=s2
else: print("invalid string choice")
y=input("select the character you want to count\n")
a=y.upper()
b=y.lower()
print(a)
result=scelta.count(a)+scelta.count(b)
print(result)

"""
#più versatile
s=input("Write your string: \n")
c=input("Which character do you want to count? (no distinction in capitalization)\n")
result=s.count(c.lower())+s.count(c.upper())
print(result)
"""