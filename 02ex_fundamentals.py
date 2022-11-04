
print("\nex. 1")

def f(alist):
    x=5
    alist1 = [alist[0],alist[1],alist[2]]
        
    for i in range(x):
        alist1.append(i)
    return alist1

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has NOT been changed





print("\nex. 2")

# Rewrited expression using a list comprehension
ans = [ x*x for x in range(10) if (x*x % 2 == 1) ] 

print(ans)





print("\nex. 3")

def f(wordsList, n):
    def lenn(stringa):
        if len(stringa)<n:
            return stringa
        return
    return list(filter(lenn, wordsList))
    
lista = ["flower","sun","water","swimming","programming"]
n = 4
ans = f(lista, n)
print(ans)



    

print("\nex. 4")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def f (dic):
    return list(map(len,dic.keys()))

ans = f(lang)
print(ans)





print("\nex. 7")

def hello(func):
    def wrapper(x): 
        print("Hello World!")
        return func(x)    
    return wrapper
    
@hello 
def square(x):
    return x*x
    
print(square(2))  







listFib = [0, 1] #The sequence commonly starts from 0 and 1

i=2

while i < 20:
	listFib.append(listFib[i-1]+listFib[i-2])
	i += 1
	
print(listFib)




def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

def fibList(n,b=[]):
    for i in range(n):
        b.append(fib(i))
    return b
    
a =[] 
n = 20
ans = fibList(n,a)

print(ans)





print("\nex. 10")


class polygon:
    x = []
    
    def __init__(self, components):
        for i in components:
            if i>0:
                self.x.append(i)
    
    # Definition of the methods
    
    def getDimension(self):
        return self.x
    
    
    def getX(self, n): # n is the component index
        return self.x[n]
     
    def setX(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.x):
            self.x[n] = xi
    
    def perimeter(self):
        return sum(self.x)
        
    def getOrderedSides(self,increasing):
        y = self.getDimension()
        
        if increasing:
            y.sort()
        else:
            y.sort(reverse=True)
        return y

# End of the class definition

b=[2,3,-2,-5,8,7,3]
a = polygon(b)
print("Perimeter:", a.perimeter())
print("Sides Ordered:", a.getOrderedSides(increasing=True))


print("\nex. 11")

class rectangle(polygon):
    def area(self):
        return self.x[0]*self.x[1]
        
c = rectangle(b)
print(c.area())

