from timeit import timeit


def esercizio1():
    #Convert the function into a pure function with 
    #no global variables or side effects
    def f(alist):
        x = 5
        lista=alist
        lista=list(lista)
        l=[]
        for element in lista: 
            l.append(element)
        for i in range(x): 
            l.append(i)
        return l

    alist = [1,2,3]
    print (f(alist))
    print (alist)

def esercizio2():
    #Write the following expression using a list comprehension:
    #`ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`
    ans=[x*x for x in range(10) if x%2==1]
    print(ans)

def esercizio3(n=6):
    #Using the `filter()` hof, define a function that takes a 
    #list of words and an integer `n` as arguments, and returns a list of words 
    #that are shorter than `n`.
    lista=["Automobile","Autista","The","Caffe"]
    minori=list(filter(lambda a: len(a)<n,lista))
    print(minori)

def esercizio4():
    #Consider the following dictionary:
    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

    #Write a function that takes the above dictionary 
    #and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.
    def func(key):
        return len(key)
    print(list(map(func,lang.keys())))

def esercizio5():
    #Write a Python program that sorts the following list of 
    #tuples using a lambda function, according to the alphabetical 
    #order of the first element of the tuple:

    language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
    language_scores.sort(key = lambda x : x[0])
    print(language_scores)
    #Hint: use the method `sort()` and its argument `key` of the `list` 
    #data structure.
    
def esercizio6(x=2):
    #Write two functions: one that returns the square of a number
    #and one that returns its cube.

    #Then, write a third function that returns the number raised
    #to the 6th power, using only the two previous functions.
    def square(x):
        return x**2
    
    def cube(x):
        return x**3
    def power_6th(x):
        return cube(square(x))

    print(power_6th(x))

def esercizio7():
    #Write a decorator named `hello` that makes every wrapped 
    # function print “Hello World!” each time the function is called.


    def hello(func):
        def square(x=2):
            func()
            return x*x
    return square

    @hello
    def Hello_World():
        print("hello world")

    print(Hello_World())

def esercizio8():
    #Calculate the first 20 numbers of the 
    #Fibonacci sequence using a recursive function.
    def recursive_Fib(a,b,counter=2):
        if counter==2:
            print(a)
            print(b)
        if counter==20:
            return print("end")
        else:
            c=b
            b=a+b
            a=c
            print(b)
            recursive_Fib(a,b,counter+1)
            
    recursive_Fib(1,1)

def esercizio9():
    #Run both the Fibonacci recursive function from the previous 
    #exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.

    #Measure the execution code of the two functions with `timeit`
    #which one is the most efficient implementation? By how much?

    #Per avere una funzione che sia self contained, 
    #copio le due funzioni all'interno di questa:
    def recursive_Fib(a=1,b=1,counter=2):
        if counter<20:
            c=b
            b=a+b
            a=c
            recursive_Fib(a,b,counter+1)

    def iteration_Fib():
        a=1;
        b=1;
        for i in range(0,18):
            c=a+b;
            a=b;
            b=c;
    t_it=timeit(iteration_Fib)
    t_rc=timeit(recursive_Fib)
    print("Iterazione"+str(t_it))
    print("Ricorsione"+str(t_rc))
    if t_rc>t_it:
        print("La Piu veloce è l'iterazione con un vantaggio del "+str(((t_rc-t_it)/t_rc)*100)+"%")
    else:
        print("La Piu veloce è la ricorsione con un vantaggio del "+str(((t_it-t_rc)/t_it)*100)+"%")

#Esercizio10
class polygon:
    def __init__(self, tupla):
        self.sides=tupla
        self.checkSide()

    def checkSide(self):
        if type(self.sides)==type(1):
            self.GetSide()
        else:
            if len(self.sides)<3:
                self.GetSide()

    def GetSide(self): #This method add sides if sides<3
        element=float(input("Add a side"))
        if type(self.sides)==type(1):
            pass
            a=(self.sides,element)
            self.sides=a
        else:
            list_a = list(self.sides)
            list_a.append(element)
            self.sides=tuple(list_a)
        self.checkSide()

    def Perimeter(self):
        Perimeter=0
        for Side in self.sides:
            Perimeter=Perimeter+Side
        return Perimeter

    def getOrderedSides(self, increasing=True):
        list_a = list(self.sides)
        if increasing ==True: list_a.sort(reverse=False)
        elif increasing == False: list_a.sort(reverse=True)
        return tuple(list_a)


#Esercizio 11
class rectangle(polygon):
    def __init__(self, tupla):#La tupla dovvrà avere dim=2 (due lati )
        super().__init__(tupla)

    def checkSide(self):
        if type(self.sides)==type(1):
            super().GetSide()
        else:
            if len(self.sides)>2:
                print("La tupla contiene troppi elementi")
                print("Per gestire questo tipo di errore, l'area verra calcolata solo sui primi due elementi")

    def Area(self):
        return self.sides[0]*self.sides[1]
