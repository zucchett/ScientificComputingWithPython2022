import math as m

#TASK 1A
helloworld = []
for i in range(1,101):
    if i%3==0 and i%5==0:
        helloworld.append("HelloWorld")
    elif i%3==0:
        helloworld.append("Hello")
    elif i%5==0:
        helloworld.append("World")
    else:
        helloworld.append(i)  
print(helloworld)


#TASK 1B
pw_list = []
for s in helloworld:
    if s == "Hello":
        pw_list.append("Python")
    elif s == "World":
        pw_list.append("Works")
    elif s == "HelloWorld":
        pw_list.append("PythonWorks")
    else:
        pw_list.append(s)
pythonworks = tuple(pw_list)
print(pythonworks)


#TASK 2
def swap(x,y):
    x,y=y,x
    return x,y

x = input("Insert x: ")
y = input("Insert y: ")

x,y = swap(x,y)
print(x,y)



#TASK 3
def euc(u,v):
    return m.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
u = (3,0)
v = (0,4)
print(euc(u,v))



#TASK 4
def ch_count(string):
    ch_dic = {}
    for ch in string.lower():
        if ch in ch_dic.keys():
            ch_dic[ch] += 1
        else:
            ch_dic[ch] = 1
    return ch_dic

s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#Printing in alphabetical order
print("String 1")
s1_dic = ch_count(s1)
for key,value in sorted(s1_dic.items()):
    print(key,value)
print()
print("String 2")
s2_dic = ch_count(s2)
for key,value in sorted(s2_dic.items()):
    print(key,value)


#TASK 5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_l = set(l)

print("Unique numbers count:")
print(len(unique_l))

print("Unique numbers in list:")
print(unique_l)



#TASK 6
a = input("Insert variable a: ")
b = input("Insert variable b: ")

try:
    var1 = int(a) #a is an int
except ValueError:
    try:
        var1 = float(a) #a is a float
    except ValueError:
        var1 = a #a is a string
try:
    var2 = int(b) #b is an int
except ValueError:
    try:
        var2 = float(b) #b is a float
    except ValueError:
        var2 = b #b is a string   

try:
    added = var1+var2
    print("Addition gave:",added)
except:
    print("Addition was not possible")




#TASK 7
#for loop
x1 = []
for x in range(0,11):
    x1.append(x**3)
print(x1)

#List comprehension
x2 = [x**3 for x in range(11)]
print(x2)



#TASK 8
a = [(i,j) for j in range(4) for i in range(3)]
print(a)



#TASK 9
triples = tuple([(a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2+b**2==c**2])
print(triples)




#TASK 10
def norm_vec(Nvec):
    squaredsum = sum([x**2 for x in Nvec])
    return tuple([x/m.sqrt(squaredsum) for x in Nvec])

print(norm_vec((3,4,5)))





#TASK 11
#Solutions using while and list
fib1 = [0,1]
while len(fib1)<20:
    fib_new = fib1[-1]+fib1[-2]
    fib1.append(fib_new)
print(fib1)

#Another possible solution (Iterative methods)
fib2 = [0,1]
a,b = 0,1
for i in range(18):
    a,b = b,a+b
    fib2.append(b)
print(fib2)

