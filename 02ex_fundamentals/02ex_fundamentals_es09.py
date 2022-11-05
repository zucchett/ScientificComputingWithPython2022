import timeit
import time


#with while
def whilefibonaci (count):
    a =0
    x=0
    y=1
    l =[]
    l.append(0)

    while a< count:
        z = x+y
        x=y
        y=z
        a += 1
        l.append(x)
    print(l)
print(timeit.timeit(stmt='whilefibonaci(20)',setup='', number=1, globals=globals()))


#with recursive function
def func(n):
    if n<2:
        return n
    else:
        return func(n-1) + func (n-2)
a =list (map(func,range(20)))
print(a)
print(timeit.timeit(stmt='a =list (map(func,range(20)))',setup='', number=1, globals=globals()))

#here we repeat timing so we can have a better conclution

print(timeit.repeat(stmt='whilefibonaci(20)',setup='',repeat = 6, number=1, globals=globals()))

print(timeit.repeat(stmt='a =list (map(func,range(20)))',setup='',repeat =6, number=1, globals=globals()))

#The recursive function is the more effiecient one
