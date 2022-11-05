# Cecilia Rossi      mat 2091484
############################ 02 EX FUNDAMENTALS ################################

####### Exercise 1

def f(alist, x):
    blist = alist[:]
    for i in range(x):
        blist.append(i)
    return blist

alist = [1,2,3]
ans = f(alist,5)
print(alist)
print(ans)

####### Exercise 2

ans = [x*x for x in list(filter(lambda y : y % 2 == 1, range(10)))]
print(ans)

####### Exercise 3

def wlist_shorter_n(wlist,n):
    wlist_short = list(filter(lambda x: len(x) <= n , wlist))
    return wlist_short

#Test
n = 5;
wlist = ['mamma','cameriere','ciao','bu','australopiteco'] #aggiungo lista di parole
print(wlist_shorter_n(wlist,n))

####### Exercise 4

def len_keys(dizio):
    return list(map(len,dizio.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(len_keys(lang))

####### Exercise 5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x:x[0])
print(language_scores)

####### Exercise 6

def square(x):
    return x**2

def cube(x):
    return x**3

def sixth(x):
    return square(cube(x))

####### Exercise 7

def hello_world(function):
    def wrapper(*args):
        func = function(*args)
        print('Hello World!')
        return func
    return wrapper

@hello_world
def square(x):
    return x*x

####### Exercise 8

def recursive_Fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else:
        return recursive_Fibonacci(n-1) + recursive_Fibonacci(n-2)

def list_recursive_Fibonacci(n):
    fibonacci = []
    for i in range(n):
        fibonacci.append(recursive_Fibonacci(i))
    return fibonacci

n = 20;
print(list_recursive_Fibonacci(n))

####### Exercise 9

import timeit

def loop_Fibonacci(n):
    for i in range(20):
        if i == 0: 
            old_fibonacci = 0
            new_fibonacci = 1
        else:
            a = new_fibonacci
            new_fibonacci = new_fibonacci + old_fibonacci
            old_fibonacci = a
    return new_fibonacci

def recursive_Fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else:
        return recursive_Fibonacci(n-1) + recursive_Fibonacci(n-2)

n = 20
loops = 1000

t_loop = timeit.timeit('loop_Fibonacci(n)', globals = globals(), number = loops)
time_loop = t_loop/loops
t_rc = timeit.timeit('recursive_Fibonacci(n)', globals = globals(), number = loops)
time_rc = t_rc/loops

print('Loop: ', str(time_loop))
print('Recursive: ', str(time_rc))
if time_loop < time_rc:
    print('The most efficient algorithm is the iterative one, with an advace of ',str(abs(time_rc - time_loop)/time_rc*100),' %')
else:
    print('The most efficient algorithm is the recursive one, with an advace of ',str(abs(time_loop - time_rc)/time_loop*100),' %')

####### Exercise 10

#Definition of the class Polygon

class Polygon:
    
    def __init__(self, length_sides):
        if len(length_sides) < 3:
            raise Error("Error: the polygon cannot be created")
        else: 
            self._length_sides = list(length_sides)
            self._num_sides = len(self._length_sides)
    
    def getSides(self):
        return self._length_sides
    
    def numSide(self):
        return self._num_sides
    
    def setSide(self, i, lunghezza):
        if i < 0 or i > self._num_sides:
            return 'Error: the index is not correct'
        else:
            self._length_sides[i] = lunghezza
    
    def perimeter(self):
        return sum(self._length_sides)
    
    def getOrderedSides(self, increasing = True):
        return tuple(sorted(self._length_sides, reverse = (not increasing)))

#Test of the class

triangolo = Polygon((5,3,4))
print('Perimetro: ', str(triangolo.perimeter()))
print('Risposta Corretta:', str(12))
print(triangolo.getSides())
print(triangolo.getOrderedSides())
print(triangolo.getSides()) #per controllare che non si modifichi la variabile di attributo

####### Exercise 11

class Rectangle(Polygon): 
    
    def __init__(self, length_sides):
        super().__init__(length_sides)
        if self.getSide != 4:
            raise Error("A Rectangle must have 4 sides")
        elif (self.getOrderedSides(0) != self.getOrderedSides(1)) or (self.getOrderedSides(2) != self.getOrderedSides(3)):
            raise Error("I lati di un Rettangolo devono essere a due a due identici")
    
    def area(self):
        return self.getOrderedSides(0)*self.getOrderedSides(2)
