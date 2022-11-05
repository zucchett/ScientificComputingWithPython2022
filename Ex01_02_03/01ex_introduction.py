#Task 1a
l=[]
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        l.append('HelloWorld')
    elif  x % 5 == 0:
        l.append('World')
    elif x % 3 == 0:
        l.append('Hello')
    else:
        l.append(x)   

#Printing results of the task 1a
print(l)

#Put results in tuple
print()
before_change=tuple(l)
print(before_change)


#Task 1b
print("List before change:")
print(l)
for i in range(len(l)):
    if(l[i]=='Hello'):
        l[i]='Python'
    elif(l[i]=='World'):
        l[i]='Works'
    elif(l[i]=='HelloWorld'):
        l[i]='PythonWorks'
print()
print('List after change:')
print(l)

#saved results in the new tuple after replacing strings
#Printing results in tuple for the task 1b
print('Final results after all change saved in tuple:')
result_tuple=tuple(l)
print(result_tuple)

#######################################################################
#Task 2
a=int(input('Set the value of the first number: '))
b=int(input('Set the value of the second number: '))
def swap(x,y ):
    
    x=x+y
    y=x-y
    x=x-y

    print("First number after change x=",x)
    print("Second number after change y=",y)
    
swap(a,b)


########################################################################

#Task 3

import math 
def eud_distance(u,v):
    result=math.sqrt(pow((u[0]-v[0]),2)+ pow((u[1]-v[1]),2))
    return result

u=(3,0)
v=(0,4)
eud_distance(u,v)
print(eud_distance(u,v))

#######################################################################

#Task 4

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


#Task 4-string 1
#we have to ignore casesensitivity, so let's covert text in lower cases
s1=s1.lower()
unique_char1=set(s1)
unique_char1=list(unique_char1)
print('Unique charachters in the string 1:')
print(unique_char1)


for i in range(len(unique_char1)):
    d= s1.count(unique_char1[i])
    print('Charachter: ' , unique_char1[i], ' occurs: ' , d)    
    
#Task 4, string 2
s2=s2.lower();
uniq_char2=set(s2);
#we need to convert set in the list
uniq_char2=list(uniq_char2)
print('Unique characters of the string2')
print(uniq_char2)

for i in range(len(uniq_char2)):
    x=s2.count(uniq_char2[i])
    print('Charachter: ' , uniq_char2[i], ' occurs: ' , x)

########################################################################
#Task 5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#Calculating how many times numbers occurs in the list and represents it like pair key:value in dictionary, where key is number
x={}
for i in l:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x) 

#Task 5
#Finding unique numbers 
l1=[]
for key, val in x.items():
    if val==1:
        l1.append(key)
        
l1.sort()        
print("Unique numbers in the list:",l1)

##########################################################################
#Task 6

try:
    x=input('Set the value of the x: ')
    y=input('Set the value of the y: ')
    
    if x.isdigit() and y.isdigit():
        
        x=int(x)
        y=int(y)
        b= x + y
        print(b)
        
    elif ('.' in x or '.' in y) or ('-' in x or '-' in y) :
        x=float(x)
        y=float(y)
        b= x + y
        print(b)
        
    else:
        b= x + y
        print(b)
    
except Exception as e:
    print(e)
    print('It is not possible to sum ', x, ' and ' , y)

####################################################################
#Task 7

#Task 7a
l2=[]
for i in range (10):
    l2.append(i)
    
print(l2)    

for i in range (len(l2)):
    l2[i]=i*i*i

print(l2)

#Task 7b

l3=[i for i in range(0,10)]
print(l3)

for i in range (0,len(l3)):
    l3[i]=pow(i,3)
print(l3)

l4=[i*i*i for i in range(0,10)]
print(l4)

#####################################################################
#Task 8
#Example given by professor

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#Task 8 solved by me, replacing professor's code
a = [(i,j) for i in range(0,3) for j in range (0,4)]
print(a)

#####################################################################
#Task 9
result=[(a,b,c) for a in range(1,100) for b in range(a+1,100) for c in range(1,100) if a**2 + b**2 == c**2 and c<100 ]
tup=tuple(result)
print(tup)

########################################################################
#Task 10

#Task 10
import math
def norm(x):
    xi_squared=[i**2 for i in x]
    sum_of_xi_squared=sum(xi_squared)
    n=math.sqrt(sum_of_xi_squared)
    result=[i/n for i in x]
    return tuple(result)
vec=[1,2,3]
a=norm(vec)

print(norm(vec))
s=[i**2 for i in a]
print(sum(s))
###########################################################################
#Task 11
#we set the value of i to calculate Fibonacci's number 
i = 1
num1, num2=0,1
print("First 20 Fibonacci numbers:")
while i < 21:
    
    print(num1)
    next = num1 + num2
    
    # update values
    num1 = num2
    num2 = next
    i+= 1




