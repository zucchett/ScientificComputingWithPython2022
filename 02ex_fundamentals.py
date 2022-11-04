#EXERCISE 1
print('\n'+'_________ESERCIZIO_1__________')
x=5
def f(alist):
    blist=alist[:]
    for i in range(x):
        blist.append(i)
    return blist
alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


#EXERCISE 2
print('\n'+'_________ESERCIZIO_2__________')
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
d=[x * x for x in range(10) if x % 2 == 1]
print(d)


#EXERCISE 3
print('\n'+'_________ESERCIZIO_3__________')
words=["ciao", "hello", "buongiorno"]
n=6
ans=list(filter(lambda w:len(w)<n, words))
print(ans)


#EXERCISE 4
print('\n'+'_________ESERCIZIO_4__________')
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
ans=list(map(lambda x:len(x),lang.keys()))
print(ans)


#EXERCISE 5
print('\n'+'_________ESERCIZIO_5__________')
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x:x[0])
print(language_scores)

#EXERCISE 6
print('\n'+'_________ESERCIZIO_6__________')
square = lambda x: x**2
cube= lambda x: x**3
six= lambda x: square(cube(x))
print(six(10))



#EXERCISE 7
print('\n'+'_________ESERCIZIO_7__________')
def hello(func): # takes a function as an argument
    def wrapper(x):
        print("Hello World!")
        func(x) # runs the function
    return wrapper # returns a function
@hello
def square(x):
    return x*x

square(3)


#EXERCISE 8
print('\n'+'_________ESERCIZIO_8__________')
def fib_rec(x):
    if x==0 or x==1:
        return x
    else:
        return fib_rec(x-2)+fib_rec(x-1)

for i in range(1,21):
    print(fib_rec(i))

#EXERCISE 9
print('\n'+'_________ESERCIZIO_9__________')
import timeit
def recursiveFibonacci(n):
    for i in range(1,n+1):
        print(fib_rec(i))
def loopFibonacci(n):
    l=[1,1]
    i=2
    while i<n:
        l.append(l[i-2]+l[i-1])
        i+=1
    print(l)

def fib_rec(x):
    if x<=1:
        return x
    else:
        return fib_rec(x-2)+fib_rec(x-1)


#%timeit loopFibonacci(20)
# 198 µs ± 60.9 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each#loop20: 126 µs ± 12.5 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

#%timeit recursiveFibonacci(20)
#14 ms ± 1.11 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)

#loop more efficient
#there is a difference of two order of magnitude for n=20, instead for larger value of n the difference
# increaseas: for example there is a difference of four order of magnitude for n=30

#EXERCISE 10
print('\n'+'_________ESERCIZIO_10__________')
class polygon:

    x = ()
    global increasing

    def __init__(self, components):
        self.x = components # a tuple is expected as input

    # Methods to get and set the length of each side
    def getDimension(self,n):
        return self.x[n]

    # This method returns the perimeter of the polygon
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p += self.x[i]
        return p

    # This method returns a tuple containing the length
    # of the sides arranged in increasing or decreasing order,
    # depending on the argument of the method
    def getOrderedSides(self,increasing):
        if increasing==True:
            l=list(self.x)
            l.sort()
            t=tuple(l)
            return t
        elif increasing==False:
            l=list(self.x)
            l.sort(reverse=True)
            t=tuple(l)
            return t
        else:
            return 'Invalid input'


# End of the class definition

a=polygon((1,3,2))

print('Perimeter= '+str(a.perimeter()))
print('Edge= '+str(a.getDimension(1)))
print(a.getOrderedSides(increasing=False))



#EXERCISE 11
print('\n'+'_________ESERCIZIO_11__________')
class rectangle(polygon):

    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, components):
        l=list(components)
        l.sort()
        if len(components) == 4 and l[0]==l[1] and l[2]==l[3]:
            self.x = components # a tuple is expected as input
        else:
            print("This is not a rectangle")

    # New methods that only belong to the child class
    def area(self):
        l=list(self.x)
        l.sort()
        return l[0]*l[2]




r=rectangle((2,3,2,3))
print('Area= '+str(r.area()))

