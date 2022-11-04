# Q1

ans = []
for i in range(3):
    for j in range(4):
        ans.append((i, j))
print(ans)

# 2
ans = [x*x for x in range(10) if x%2 == 1]
print(ans)

# Q2

def f(alist):
    
    x = 5
    k = alist.copy()
    for i in range(x):
        k.append(i)
    return k

alist = [1,2,3]
ans = f(alist)

print (ans)
print (alist)


# Q3

words = ["araba","tren","taklaci","anten","saat","tatli","italia"]
n = int(input("Please enter a number:"))
def myFunc(word, n):
    return len(word) < n
print(list(filter(lambda seq: myFunc(seq, n),words)))

# Q4

def lenght(n):
    a=list(map(len,n))
    return a
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(lenght(lang))

# Q5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x : x[0])
print(language_scores)

# Q6

def three(n):
    cube=n**3

    def two(n):
        sqr=n**2
        return sqr

    b=two(n)
    return cube ,b

def six(n):
    sixth=a*b*n
    return sixth


x= int(input("please enter the number:")) 
a,b= three(x)
c= six(x)

print("Sixth power of x :",c)


# Q7

def hello(func):
    def wrapper(x):
        print("Hello World")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

x=square(5)
print("Result of original function: ",x)

# Q8

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

y=[]
for i in range(20):
    y.append(fibonacci(i))
print(y)


# Q9

import timeit

def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


def loopFibonacci(n):
    f=[]
    for i in range (n):
        f.append(i)
        if i>1:
            f[i]= f[i-1]+f[i-2]

def recursiveFibonacci(n):
    y=[]
    for i in range(n):
        y.append(fibonacci(i)) 
    return y 


starttime=timeit.default_timer()
loopFibonacci(20)
endtime=timeit.default_timer()
print("Timer for Fibonacci: ",(endtime-starttime))

starttime1=timeit.default_timer()
recursiveFibonacci(20)
endtime1=timeit.default_timer()
print("Timer for recursiveFibonacci: ",(endtime1-starttime1))



# Q10

from tabnanny import check
class Polygon:
    def define():
        while True:
            try:
                label: check
                number_of_side=int(input("please enter the number of Polygon:"))
                if (number_of_side < 3):
                    goto .check
                break
            except:
                print("Please enter integer or enter at least 3 sides")

        sides=[]
        for i in range (number_of_side):
            sides.append(int(input("Please enter the side lenght:")))
        tuple(sides)
        #print(sides)
        return sides    

    def perimeter(n):
        perimeter=0
        for i in range(len(n)):
            perimeter = n[i]+perimeter
        print("Perimeter of Polygon is:",perimeter)
        return perimeter

    def getOrderedSides(increasing,n):
        if increasing:
            list.sort(n)
            print("The sides of polygon are:",n)


a=Polygon.define()
Polygon.perimeter(a)
Polygon.getOrderedSides(True,a)

# Q11

from tabnanny import check
class Polygon:

    def define():
        while True:
            try:
                label: check
                number_of_side=int(input("please enter the number of Polygon:"))
                if (number_of_side != 4):
                    goto .check
                break
            except:
                label: check
                print("Please enter integer or enter 4 sides")

        sides=[]

        long=int(input("Please enter the long side lenght:"))
        short=int(input("Please enter the short side lenght:"))
        sides.append(long)
        sides.append(short)
        sides.append(long)
        sides.append(short)

        tuple(sides)
        print(sides)
        return sides    

    def perimeter(n):
        perimeter=0
        for i in range(len(n)):
            perimeter = n[i]+perimeter
        print("Perimeter of Polygon is:",perimeter)

        return perimeter


class Rectangle(Polygon):

    def Area(n):
        m= list(n)
        Area= n[0]*n[1]
        print("Area of rectangle is:",Area)
        return Area


a=Polygon.define()
Polygon.perimeter(a)
Rectangle.Area(a)