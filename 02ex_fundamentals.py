#1. Global Variables
x = 5

def f(alist):
    g = alist.copy()
    for i in range(x):
        g.append(i)
    return g

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

#2.List Comprehension
mylist = [(i**i) for i in range(10) if i % 2 ==1]
print(mylist)

#3. Filter list
mywordlist = ["Hello" , "beautiful" , "world", "my" , "home" , "is" , "here"]
print("Original wordlist: ", mywordlist)

def cut(word, n):
    return len(word)<n

def stringCutter(wordlist, n):
    shortenList = list(filter(lambda word: cut(word,n), wordlist))
    return shortenList

print("String with words whorter than 5",stringCutter(mywordlist,5))

#4. Map dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def countKeys(dict):
    keylist = dict.keys()
    keycounter = list(map(len, keylist))
    return keycounter
print(countKeys(lang))

#5. Lambda functions
l = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
def Sort_Tuple(tup):
    tup.sort(key = lambda x: x[0])
    return tup
print(Sort_Tuple(l))

#6. Nested functions
def square(number):
    number = number**2
    return number

def cube(number):
    number = number**3
    return number

print(square(cube(2)))

#7. Decorators
def hello(func):
    def wrapper(n):
        print("Hello world")
        print(func(n))
    return wrapper

@hello
def square(x):
    return x*x

#print(square(3))
square(7)
square(8)

#8.The Fibonacci sequence (part 2)
def fib_rec(n):
    if n==0 or n==1:
       return n
    return fib_rec(n-1) + fib_rec(n-2)

my_fibonacci = []

for n in range(21):
  my_fibonacci.append(fib_rec(n))

print(my_fibonacci)

#9. The Fibonacci sequence (part 3)
import timeit
start = timeit.timeit()
def fib_rec(n):
    if n==0 or n==1:
       return n
    return fib_rec(n-1) + fib_rec(n-2)

my_fibonacci = []
def myfib(n):
    for n in range(21):
        my_fibonacci.append(fib_rec(n))
    return my_fibonacci
myfib(20)
end = timeit.timeit()
print(end-start)
#2.25 µs ± 62.8 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each) with %timeit on jupyter notebook

start2 = timeit.timeit()
fibonacci = []
def loopFibonacci(n):
   for i in range(1,20):
    if n == 1:
        fibonacci = [0]
    else:
        fibonacci = [0,1]
        for i in range(1,19):
         fibonacci.append(fibonacci[i-1] + fibonacci[i])
    return(fibonacci)

loopFibonacci(20)
end2 = timeit.timeit()
print(end2-start2)
#5.9 ms ± 203 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) with %timeit on jupyter notebook
#recursive execution time is always longer than the iterative one

#10. Class definition (Part 1: Creating class)
import math

class Polygon:
      def __init__(self, components):
        self.x = components

def getSide(self, n):
    return self.x[n]

def setSide(self, n, value):
    index = n
    newpolygon = []
    for i in range(len(self.x)):
       if i == n:
        newpolygon.append(value)
       else:
        newpolygon.append(self.x[i])
    self.x = tuple(newpolygon)

def setSide2(self, n, value):
    self.x[n] = value

def perimeter(self):
    p = 0
    for i in range(len(self.x)):
       p = p + self.x[i]
    return p

def getOrderedSides(self):
    lenList = []
    for i in range(len(self.x)):
     lenList.append(self.x[i])
    lenList.sort()
    lenTuple = tuple(lenList)
    return lenTuple

def getOrderedSides2(self,increasing = True):
    lenList = list(self.x)
    lenList.sort(reverse=not(increasing))
    return tuple(lenList)

#10. Class definition (Part 2: Test Class)
newPolygon = Polygon((3,7,2,1,5))
print(perimeter(newPolygon))
print(getOrderedSides2(newPolygon,True))


# 11. Class inheritance (Part 1: Creating Class)
class Rectangle(Polygon):

    def __init__(self, components):
        if len(components) == 2:
            self.x = components
        else:
            print("Error: number of components is not 2")


def area(self):
    area = self.x[0] * self.x[1]
    return area

#11. Class inheritance (Part 2: Testing Class)
myRect = Rectangle((3,2))
print(area(myRect))
