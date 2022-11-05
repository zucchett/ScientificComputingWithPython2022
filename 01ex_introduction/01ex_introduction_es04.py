# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:33:59 2022

@author: Ruben
"""

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s3 = "abcdefghijklmnopqrstuvwxyz"

#s=input("Inserisci una stringa: ")


x = 0

i = 97
while i < 123:
    for j in range(len(s3)):
        if chr(i) == s3[j].lower() :
            x += 1
        j += 1
        
    print('The number of times ' + chr(i) + ' occurs is ', x)
    
    x=0
    i += 1
    
    
