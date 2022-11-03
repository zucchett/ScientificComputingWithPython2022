import os
import timeit

# 1. Global variables

x = 5

def f(alist):
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)
print("alist has NOT been changed")

# 2. List comprehension

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

ans2 = [map(lambda x: x*x, filter(lambda x: x % 2 == 1, range(10)))]
print(ans2)

# 3. Filter list

liste = ["İstanbul", "İzmir", "Van", "Kastamonu", "Kars", "Ankara", "Kilis"]

def shorterthan(liste, n):
    newListe = list(filter(lambda x : len(x) < n, liste))
    return newListe

print(shorterthan(liste, 4))
print(shorterthan(liste, 6))
print(shorterthan(liste, 8))

# 4. Map dictionary

liste = ["İstanbul", "İzmir", "Van", "Kastamonu", "Kars", "Ankara", "Kilis"]

def shorterthan(liste, n):
    newListe = list(filter(lambda x : len(x) < n, liste))
    return newListe

print(shorterthan(liste, 4))
print(shorterthan(liste, 6))
print(shorterthan(liste, 8))

# 5. Lambda functions

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores

language_scores.sort(key = lambda x : x[0])
print(language_scores)

# 6. Nested functions

def sqr(x):
    return x * x

def cbe(x):
    return x * x * x

def nested6thpwr(x):
    return sqr(cbe(x))

b = 2
a = nested6thpwr(b)
print(a)
a == b**6

# 7. Decorators

def hello(func):
    def wrap(x):
        print("Hello World!")
        return func(x)    
    return wrap

@hello
def square(x):
    return x*x

print(square(4))

# 8. The Fibonacci sequence (part 2)

fibonacci = []

def fibo(x):
    if x == 1 or x == 0:
        return x
    
    return fibo(x-1) + fibo(x-2)
        
for i in range(20):
    fibonacci.append(fibo(i))
    
print(fibonacci)

# 9. The Fibonacci sequence (part 3)

def ex01fibo():
    fibo = [0, 1]

    for i in range(20-2):
        fibo.append(fibo[-2] + fibo[-1])
    
    return fibo

def ex02fibo():
    fibonacci = []

    def fibo(x):
        if x == 1 or x == 0:
            return x
    
        return fibo(x-1) + fibo(x-2)
        
    for i in range(20):
        fibonacci.append(fibo(i))
    
    return fibonacci

start_time1 = timeit.default_timer()
ex01fibo()
duration1 = timeit.default_timer() - start_time1

start_time2 = timeit.default_timer()
ex02fibo()
duration2 = timeit.default_timer() - start_time2

print(str(duration1) + "\n" + str(duration2))

print("ex01fibo is way faster than ex02fibo")

# 10. Class definition

class Polygon:
    
    lengths = []

    def __init__(self, lengths:tuple):
        if len(lengths) > 2:
            self.lengths = lengths

    def getLengths(self):
        return self.lengths

    def getX(self, n):
        if n < len(self.lengths):
            return self.lengths[n]

    def setLengths(self, n, xi):
        if n < len(self.lengths):
            self.lengths[xi] = xi

    def perimeter(self):
        return perimeter

    def getOrderedSides(self, increasing = True):
        ordered = self.lengths
        if increasing:
            ordered.sort()
        else:
            ordered.sort(reverse=True)
        return ordered

# 11. Class inheritance

print("I couldn't make this part work.")




