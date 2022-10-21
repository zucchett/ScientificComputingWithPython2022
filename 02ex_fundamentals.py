# 02ex - FILE UNICO
#Author: Riccardo Mosele 2044736
import math

#flag per l'esecuzione singola degli esercizi
active = True
passive = False



#SELEZIONARE L'ESERCIZIO DA ESEGUIRE 
#INSERIRE "active" PER ESEGUIRLO
#INSERIRE "passive" PER NON ESEGUIRLO
#E' POSSIBILE L'ESECUZIONE MULTIPLA E DI TUTTI GLI ESERCIZI


printEs1=passive  #esercizio 2.1
printEs2=passive  #esercizio 2.2
printEs3=active  #esercizio 2.3
printEs4=passive  #esercizio 2.4
printEs5=passive  #esercizio 2.5
printEs6=passive  #esercizio 2.6
printEs7=passive  #esercizio 2.7
printEs8=passive  #esercizio 2.8
printEs9=passive  #esercizio 2.9
printEs10=passive #esercizio 2.10
printEs11=passive #esercizio 2.11



#***************************************************Ex 2.1
if(printEs1):
    print("\n\n***************************************************Ex 2.1")

    def f(alist, x):
        tmpList=[i for i in alist]
        for i in range(x):
            tmpList.append(i)
        return tmpList

    alist = [1, 2, 3]
    ans = f(alist, 5)
    print(ans)
    print(alist) # alist has not been changed


#***************************************************Ex 2.2
if(printEs2):
    print("\n\n***************************************************Ex 2.2")

    ans = list(map(lambda x: x * x,
    filter(lambda x: x % 2 == 1, range(10))))
    print(f"With map and filter:\n{ans}")

    list=[x*x for x in range(10) if x % 2 == 1]
    print(f"\nWith list List comprehension:\n{list}")

#***************************************************Ex 2.3
if(printEs3):
    print("\n\n***************************************************Ex 2.3")

    listWord = ["Ciao", "Buongiorno", "Buonasera", "Buonanotte", "Salve"]

    try:
        x = int(input("Insert the max lenght: "))
        res=[]
        for i in filter(lambda y: len(y)<int(x), listWord):
            res.append(i)
        print(res)
    except:
        print("ERROR: Insert an integer value!")

    
#***************************************************Ex 2.4
if(printEs4):
    print("\n\n***************************************************Ex 2.4")

    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    print(f"length of the keys: {list(map(lambda y: len(y),lang))}")

#***************************************************Ex 2.5
if(printEs5):
    print("\n\n***************************************************Ex 2.5")

    language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

    language_scores.sort(key = lambda x: x[0])
    print(f"Alphabetical order of first element: \n{language_scores}")


#***************************************************Ex 2.6
if(printEs6):
    print("\n\n***************************************************Ex 2.6")

    def square(a):
        return a*a

    def cube(b):
        return b*b*b

    def sixth(c):
        return square(cube(c))

    print(f"two at 6th power: {sixth(2)}")


#***************************************************Ex 2.7
if(printEs7):
    print("\n\n***************************************************Ex 2.7")

    def hello(func):
        def wrapper(x):
            print("Hello World")
            return func(x)
        return wrapper

    @hello
    def square(x):
        return x*x

    x=square(2)
    print(f"Res function: {x}")


#***************************************************Ex 2.8
if(printEs8):
    print("\n\n***************************************************Ex 2.8")

    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    fibSeq=[]
    for i in range(20):
        fibSeq.append(fib(i))

    print(f"First {len(fibSeq)} numbers of Fibonacci sequence:\n{fibSeq}")
    

#***************************************************Ex 2.9
import timeit
if(printEs9):
    print("\n\n***************************************************Ex 2.9")

    def loopFibonacci(m):
        fibSeq=[1,1]
        for i in range(m):
            fibSeq.append(fibSeq[len(fibSeq)-1]+fibSeq[len(fibSeq)-2])
        return fibSeq

    def recurviveFibonacci(m):
        def fib(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            else:
                return fib(n-1) + fib(n-2)

        fibSeq=[]
        for i in range(m):
            fibSeq.append(fib(i))
        return fibSeq

    resLoop = timeit.timeit(stmt='loopFibonacci(20)', globals=globals(), number=1)
    resRec = timeit.timeit(stmt='recurviveFibonacci(20)', globals=globals(), number=1)

    print(f"With LOOP: {resLoop}")
    print(f"With RECURSIVE{resRec}")



#***************************************************Ex 2.10
if(printEs10):
    print("\n\n***************************************************Ex 2.10")

    class polygon:
        pol=[]

        def __init__(self, data):
            if(len(data)<3):
                print("Insert at least 3 element!")
                self.__del__()
            self.pol=list(data)

        def __del__(self):
            print("Goodbye")

        def getSide(self, pos):
            pos=pos-1
            if(pos<0):
                print("ERROR: wrong value")
                return 0
            else:
                return self.pol[pos]

        def setSide(self, pos, value):
            pos=pos-1
            if(pos<0):
                print("ERROR: wrong value")
            else:
                self.pol[pos]=value

        def perimeter(self):
            per=0
            for i in self.pol:
                per=per+i
                print(per)
            return per

        def getOrderedSides(self, increasing):
                return tuple(sorted(self.pol,reverse=not increasing))

        def printAll(self):
            print(self.pol) 

      
    x = polygon((40,10,20,50,7))
    print("Initial polygon: ")
    x.printAll()

    print("\nInsert the new value 30 instead 7 (last side)")
    x.setSide(5,30)

    print("New polygon: ")
    x.printAll()

    print(f"\nPerimeter: {x.perimeter()}")

    print("\nSort in increasing and decreasing order: ")
    tmp = x.getOrderedSides(increasing = True)
    print(tmp)

    tmp = x.getOrderedSides(increasing = False)
    print(tmp)

    print("\nPolygon:")
    x.printAll()

    
    
#***************************************************Ex 2.11
if(printEs11):
    print("\n\n***************************************************Ex 2.11")

    class polygon:
        pol=[]

        def __init__(self, data):
            if(len(data)<3):
                print("Insert at least 3 element!")
                self.__del__()
            self.pol=list(data)

        def __del__(self):
            print("Goodbye")

        def getSide(self, pos):
            pos=pos-1
            if(pos<0):
                print("ERROR: wrong value")
                return 0
            else:
                return self.pol[pos]

        def setSide(self, pos, value):
            pos=pos-1
            if(pos<0):
                print("ERROR: wrong value")
            else:
                self.pol[pos]=value

        def perimeter(self):
            per=0
            for i in self.pol:
                per=per+i
                print(per)
            return per

        def getOrderedSides(self, increasing):
                return tuple(sorted(self.pol,reverse=not increasing))

        def printAll(self):
            print(self.pol) 

    class rectangle(polygon):

        def __init__(self, data):
            if(len(data)==2):
                self.pol=list(data)
                self.pol.append(data[0])
                self.pol.append(data[1])
            else:
                print("Insert 2 element: base and height")
                self.__del__()

        def area(self):
            return self.pol[0]*self.pol[1]


    myRect = rectangle((10,20))

    print("Print all side of rect: ")
    myRect.printAll()

    print(f"\nArea:{myRect.area()}")