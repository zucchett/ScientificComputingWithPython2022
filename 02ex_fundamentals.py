#ex 1

print("")
print("Global variables")
print("")

x = 5

def f(l):
    l1 = []
    for i in range(len(l)-1):
        l1.append(l[i])
    for j in range(x):
        l1.append(j)
    return l1

l = [1, 2, 3]
l1 = f(l)
print('modified list',l1)
print('original',l)

#ex 2

print("")
print("List comprehension")
print("")

ans = [x*x for x in range(10) if x*x % 2 == 1]
print(ans)

#ex 3

print("")
print("Filter list")
print("")

from random import randint

n = randint(1,10)
l = ['hot', 'baby', 'cannot', 'create', 'jump', 'incredible', 'expectations', 'a', '']

def shorter(e):
    if len(e) < n:
        return True
    else:
        return False

eliminator = filter(shorter,l)
l1 = []

for m in eliminator:
    l1.append(m)


print("n:",n)
print("original list:",l)
print("filtered list:",l1)

#ex 4

print("")
print("Map dictionary")
print("")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def keylen(a_dict):
    key_list = list(a_dict.keys())
    keylen_list = map(lambda x: len(x),key_list)
    return list(keylen_list)

print(keylen(lang))

#ex 5

print("")
print("Lambda functions")
print("")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

print(sorted(language_scores, key=lambda language: language[0]))

#ex 6

print("")
print("Nested functions")
print("")

squared = list(map(lambda x: pow(x,2), range(10)))
cubed = list(map(lambda x: pow(x,3), range(10)))
print(squared)
print(cubed)

def sixth(cubed):
    numbers = []
    for i in range(len(cubed)):
        numbers.append(pow(cubed[i],2))
    return numbers

print(sixth(cubed))

#ex 7

print("")
print("Decorators")
print("")

def hello(func):
    def wrapper(*args):
        func(*args)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    return x*x

square(5)

#ex 8

print("")
print("The Fibonacci sequence (part 2)")
print("")

def recursivefibonacci(n):

    if n < 2 :
        return n
    return recursivefibonacci(n-2) + recursivefibonacci(n-1)

l = []
for i in range(20):
    l.append(recursivefibonacci(i))

print('recursivefib:',l)

#ex 9

print("")
print("The Fibonacci sequence (part 3)")
print("")

def loopfibonacci(n):

    if n < 2 :
        return n
    fib0 = 0
    fib1 = 1
    for i in range(2, n+1) :
        newFib = fib0 + fib1
        fib0 = fib1
        fib1 = newFib
    return fib1

l = []
for i in range(20):
    l.append(loopfibonacci(i))

print('loopfib:',l)

from time import perf_counter

beginTime1 = perf_counter()
mode1 = recursivefibonacci(n)
endTime1 = perf_counter()
Time1 = endTime1 - beginTime1
beginTime2 = perf_counter()
mode2 = loopfibonacci(n)
endTime2 = perf_counter()
Time2 = endTime2 - beginTime2
print("")
print("metodo iterativo:",Time2," metodo ricorsivo:",Time1)

#ex 10

print("")
print("Class definition")
print("")

class polygon:

    x = []

    def __init__(self, tupla):

        if len(tupla) >= 3:
            self.x = list(tupla)
        else:
            print("Error: number of components is under 3")

    def getLenght(self, n):

        return self.x[n]

    def setLenght(self, n, xi):

        if n < len(self.x):
            self.x[n] = xi

    def perimeter(self):

        perimeter = 0
        for i in range(len(self.x)):
            perimeter = perimeter + self.x[i]
        return perimeter

    def getOrderedSides(self, increasing = True):

        y = []
        z = list(self.x)
        i = 0
        if increasing:
            while i < len(z):
                y.append(min(z))
                z.remove(min(z))
        else:
            while i < len(z):
                y.append(max(z))
                z.remove(max(z))
        return tuple(y)

a = polygon((4,5,8))
print('perimetro:',a.perimeter())
print('lati ordinati:',a.getOrderedSides())

#ex 11

print("")
print("Class inheritance")
print("")

class rectangle(polygon):

    def __init__(self, tupla):

        if len(tupla) != 4:
            print("Error: number of components is not 4")
        else:
            self.x = list(tupla)
            for i in range(len(self.x)):
                if self.x.count(self.x[i]) != 2:
                    return print("Error: it is not a rectangle")


    def area(self):

        area = min(self.x)*max(self.x)
        return area

b = rectangle((4,7,7,4))
print("perimetro:",b.perimeter())
print("lati ordinati:",b.getOrderedSides())
print("area:",b.area())
