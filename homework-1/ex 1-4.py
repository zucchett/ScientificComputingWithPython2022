# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:23:35 2022

@author: gozde
"""

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

all_freq = {}
  
for i in s1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
print ("Count of all characters in s1 is  :/n"
                                        +  str(all_freq))

for i in s2:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
print ("Count of all characters in s2 is :\n "
                                        +  str(all_freq))