# %% [markdown]
# # exercise 1a

# %%
count = 1
while (count < 101):
    if count%3 == 0:
        print('Hello')
    elif count%5==0:
        print('World')
    elif count%15==0:
        print('HelloWorld')
    else:
        print(count)
    count +=  1 

# %% [markdown]
# # excercise 1b

# %%
count = 1
mylist=[]
while (count < 101):
    if count%3 == 0:
        mylist.append('Hello')
    elif count%5==0:
        mylist.append('World')
    elif count%15==0:
        mylist.append('HelloWorld')
    else:
        mylist.append(count)
    count +=  1 

l=len(mylist)
i=0
while i<l:
    if mylist[i]=='Hello':
        mylist[i]='Python'
    if mylist[i]=='World':
        mylist[i]='Works'
    i+=1
mytuple=tuple(mylist)

print(mytuple)

# %% [markdown]
# #exercise 2

# %%
inputx=input('enter x: ')
print('x: '+inputx)
inputy=input('enter y: ')
print('y: '+inputy)
inputx, inputy = inputy, inputx
print('x: '+inputx+'    y: '+inputy)

# %% [markdown]
# #exercise 3

# %%
def distance2d():
  import math
  from math import sqrt
  first_point = tuple(input('Enter space-separated x and y for the first point: ').split())
  print('first point is: ',first_point)
  second_point= tuple (input('Enter space-seprated x and y for the second poinr: ').split())
  print('second point is: ', second_point)

  distance = math.sqrt( ((int(first_point[0])-int(second_point[0]))**2)+((int(first_point[1])-int(second_point[1]))**2) )

  print("distance between ", first_point,"and", second_point, "is",distance) 

distance2d()

# %% [markdown]
# #exercise 4
# 

# %%
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s=(s1.lower())+(s2.lower())
lettercounter = {i : s.count(i) for i in set(s)}
    
print ("Counter of each letter"+  str(lettercounter))

# %% [markdown]
# #exercise 5
# 

# %%
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l1 = []
count = 0
 
for item in l:
    if (l.count(item) == 1):
        count += 1
        l1.append(item)
 
print("No of unique items are:", count)
print("uniqe items are: ",l1)

# %% [markdown]
# #exercise 6  

# %%
 a=input("enter the first: ")
 b=input("enter the second ")
try:
    c=int(a) + int(b)
    print("result is",c)
except:
    try:
        c=float(a)+float(b)
        print("result is",c)
    except:
        try:
            c=a+b
            print("result is",c)
        except:
         print('the type of two argumant is not the same')



# %% [markdown]
# #exercise 7a

# %%
cubes = [x**3 for x in range(0,10)]
print(cubes)


# %% [markdown]
# #exercise 7b

# %%
cubeb=[]
for x in range(0,10):
    cubeb.append(x**3)
print(cubeb)

# %% [markdown]
# #exercise 8
# 

# %%
print([(i, j) for i in range (3) for j in range (4)])

# %% [markdown]
# #exercise 9

# %%
p  = [(a,b,c) for a in range(1,101) for b in range(a,101) for c in range(100) if a*a + b*b == c*c]
p_tuple=tuple(p)
print (p_tuple)

# %% [markdown]
# #exercise 10

# %%
import math
a = input("Enter number of vector dimension : ")
vec = []
for i in range(int(a)):
    b = input("Enter dimension sie of vector : ")
    vec.append(float(b))
print("vector is :",vec)


ms = math.sqrt(sum([x**2 for x in vec]))
n_v = []
for b in vec:
    n_v.append(b/ms)
print("Normalized vector :", n_v)

# %% [markdown]
# #exercise 11

# %%
def new_func():
    n=0
    a=0
    b=1

    while n<20:
        print(a)
        x=a+b
        a=b
        b=x
        n += 1

new_func()


