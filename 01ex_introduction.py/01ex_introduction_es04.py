#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Counting letters

#s1 = "Write a program that prints the numbers from 1 to 100. \
#But for multiples of three print Hello instead of the number and for the multiples of five print World. \
#For numbers which are multiples of both three and five print HelloWorld."
#s2 = "The quick brown fox jumps over the lazy dog"

s1=input("enter your letter")
s2=input("enter your text")
counter=0
for i in s2:
  if i==s1.lower() or i==s1.upper():
    counter+=1
    
print(counter)


# In[ ]:




