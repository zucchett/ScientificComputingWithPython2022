# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:14:29 2022

@author: 10
"""
import math 
import numpy as np
#%% QUESTION 1
# A)
numbers = list(range(1,101))
for i in range(0,100):
    if numbers[i]%3==0 and numbers[i]%5!=0 :
        numbers[i]='Hello'
    elif numbers[i]%5==0 and numbers[i]%3!=0:
         numbers[i] = 'World' 
    elif numbers[i]%15==0:
          numbers[i]= 'HelloWorld'
print(numbers)

# B)
#***Hello to Python , World to Works ***###
for i in range(0,100):
    if numbers[i]== 'Hello':
        numbers[i]='Python'
    elif numbers[i]== 'World':
        numbers[i]='Works'
print(numbers)

### converting to the tuples ####
def convert(list):
    return tuple(list)
tuple_numbers= convert(numbers)
print(convert(numbers))

#%% QUESTION 2

x = input('Enter x: ')
y = input('Enter y: ')

x,y = y,x

print('x= ' ,x , 'y=' , y )

#%% QUESTION 3
u = (3,0)
v= (0,4)

t =(u[0]-v[0])**2 + (u[1]-v[1])**2

distance = math.sqrt(t)
print('Distance=', distance)
#%% QUESTION 4

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


counts_of_letters = {}
for i in s1.lower():
    counts_of_letters[i] = s1.lower().count(i)   
print(counts_of_letters )
print( "\n")
counts_of_letters_2={}
for i in s2.lower():
    counts_of_letters_2[i]=s2.lower().count(i)
print(counts_of_letters_2)
      
#%% QUESTION 5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#using set
unique_numbers =list(set(l))

#with function
unique_numbers_with_function = np.unique(l)

#with List
unique_list=[]
for i in l:
    if i not in unique_list:
        unique_list.append(i)
       
#counting elements
counts_of_numbers = {}
for i in l:
    counts_of_numbers[i] = l.count(i)
    
print(counts_of_numbers)

#%% QUESTION 6

x = input('number: ')
y = input('number: ')

try:
    x=float(x)
    y= float(y)
    z= x+y
    print(z)
except:
 print ('cannot be added')

#%%QUESTION 7
#A)
x = list(range(0,11))
for i in range(len(x)):
    print(pow(x[i],3))
    
#B)
lst_comp = [pow(c,3) for c in x ]
#%%QUESTION 8
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

a_new=[(i,j) for i in range(3) for j in range(4) ]

#%%QUESTION 9

tuple_list = [(a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2 + b**2 == c**2]
new_tuple = tuple(tuple_list)
print(new_tuple)

#%%QUESTION 10
V_norm={}
V= (3,4,5)
V_abs=0
#finding the absolute length of vector
for i in range(len(V)):
    V_abs+= V[i]**2
V_length = math.sqrt(V_abs)
#normalizing the each element
for i in range(len(V)):
    V_norm[i] = V[i] / V_length
print(V_norm)
#checking the summation of the elements equal to 1
V_unit=0
for i in range(len(V_norm)):
    V_unit+= V_norm[i]**2
print( "\nchecking the sum of the normalized vector which resulted as:" , V_unit)

#%%QUESTION 11
num=[0,1] # we should start by knowing first 2 elements
def fibonacci(n):
    for i in range(20):
        num[i+1] = num[i]+num[i-1]
        num.append(num)
        print(num[i])

fibonacci(20)
