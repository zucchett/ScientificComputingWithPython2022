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


printEs1=active  #esercizio 2.1
printEs2=active  #esercizio 2.2
printEs3=active  #esercizio 2.3
printEs4=active  #esercizio 2.4
printEs5=active  #esercizio 2.5
printEs6=active  #esercizio 2.6
printEs7=active  #esercizio 2.7
printEs8=active  #esercizio 2.8
printEs9=active  #esercizio 2.9
printEs10=active #esercizio 2.10
printEs11=active #esercizio 2.11


#***************************************************Ex 2.1
if(printEs1):
    print("\n\n***************************************************Ex 2.1")

    def f(alist, x):
        #copio la lista originale in una temporanea
        tmpList=[i for i in alist]
        for i in range(x):
            tmpList.append(i)
        return tmpList

    alist = [1, 2, 3] #lista orignale
    ans = f(alist, 5)
    print(f"Original list: {alist}") #lista originale
    print(f"List modified by function: {ans}") #lista ottenuta dopo la funzione

#***************************************************Ex 2.2
if(printEs2):
    print("\n\n***************************************************Ex 2.2")
   
    #originale
    ans = list(map(lambda x: x * x,
    filter(lambda x: x % 2 == 1, range(10))))
    print(f"With map and filter:\n{ans}")

    #con list comprehension
    tmpList=[x*x for x in range(10) if x % 2 == 1]
    print(f"\nWith list comprehension:\n{tmpList}")

#***************************************************Ex 2.3
if(printEs3):
    print("\n\n***************************************************Ex 2.3")

    listWord = ["Ciao", "Buongiorno", "Buonasera", "Buonanotte", "Salve"]

    #inserisco da terminale il valore n (condizione: integer)
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

    #definisco il parametro per il sort tra le parentesi
    language_scores.sort(key = lambda x: x[0])
    print(f"Alphabetical order of first element: \n{language_scores}")

#***************************************************Ex 2.6
if(printEs6):
    print("\n\n***************************************************Ex 2.6")

    def square(a):
        return a*a

    def cube(b):
        return b*b*b

    #nested function:
    def sixth(c):
        return square(cube(c))

    print(f"Two at 6th power: {sixth(2)}")

#***************************************************Ex 2.7
if(printEs7):
    print("\n\n***************************************************Ex 2.7")

    #decorator:
    def hello(func):
        def wrapper(x):
            print("Hello World")
            return func(x)
        return wrapper

    #funzione originale con decoratore:
    @hello
    def square(x):
        return x*x

    x=square(2)
    print(f"Result of original function: {x}")

#***************************************************Ex 2.8
if(printEs8):
    print("\n\n***************************************************Ex 2.8")

    def fib(n):
        #casi base(primi due elementi sono 1):
        if n == 0 or n==1:
            return 1
        else:
            #chiamata ricorsiva:
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
            if n == 0 or n==1:
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
    print(f"With RECURSIVE: {resRec}")
    print(f"Loop implementation is faster than recursive implementation of:\n {resRec-resLoop}s")

#***************************************************Ex 2.10
if(printEs10):
    print("\n\n***************************************************Ex 2.10")

    class polygon:
        #pol contiene tutti i lati del poligiono
        pol=[]

        #costruttore
        #@data: lista contenente i lati del poligono, almeno 3
        def __init__(self, data):
            #il poligono deve avere almeno 3 lati
            if(len(data)<3):
                print("Insert at least 3 element!")
                self.__del__()
            self.pol=list(data) #chiamo il distruttore

        def __del__(self):
            print("Goodbye")

        #restituisce la lunghezza del lato nella posizione "pos"
        #@pos: int, inidca la posizione del lato interessato
        #@return: lunghezza del lato in "pos"
        def getSide(self, pos):
            pos=pos-1
            if(pos<0 or pos>len(self.pol)):
                print("ERROR: wrong value")
                return 0
            else:
                return self.pol[pos]

        #sostituisce la lunghezza di un determinato lato, quello nella posizione "pos"
        #@pos: int, indica la posizione del lato interessato
        #@value: float/int, è la lunghezza del lato da sostituire
        #@return: null
        def setSide(self, pos, value):
            pos=pos-1
            if(pos<0 or pos>len(self.pol)):
                print("ERROR: wrong value")
            else:
                self.pol[pos]=value

        #calcola il perimetro del poligono
        #@return: valore del perimetro
        def perimeter(self):
            per=0
            for i in self.pol:
                per=per+i
            return per

        #restituisce una tupla corrispondente al poligono, ordinata
        #@increasing: boolean, se è "true" la lista viene ordinata in modo crescente, descrescente se "false"
        #@return: tupla ordinata
        def getOrderedSides(self, increasing):
                return tuple(sorted(self.pol,reverse=not increasing))

        #stampa tutti i lati del poligono
        #@return: null
        def printAll(self):
            print(self.pol) 

      
    #definisco un poligono e lo stampo
    myPoligon = polygon((40,10,20,50,7))
    print("Initial polygon: ")
    myPoligon.printAll()

    #sostituisco la lunghezza di un lato
    print("\nInsert the new value 30 instead 7 (last side)")
    myPoligon.setSide(5,30)

    #stampo il nuovo poligono
    print("New polygon: ")
    myPoligon.printAll()

    #calcolo il perimetro
    print(f"\nPerimeter: {myPoligon.perimeter()}")

    #stampo in ordine decrescente e crescente
    print("\nSort in increasing and decreasing order: ")
    tmp = myPoligon.getOrderedSides(increasing = True)
    print(tmp)

    tmp = myPoligon.getOrderedSides(increasing = False)
    print(tmp)

    #controllo di non aver modificato il poligono originale con il riordinamento
    print("\nPolygon:")
    myPoligon.printAll()
   
#***************************************************Ex 2.11
if(printEs11):
    print("\n\n***************************************************Ex 2.11")

    class rectangle(polygon):

        #costruttor
        #@data: lista contenente base e altezza del rettangolo
        def __init__(self, data):
            if(len(data)==2):
                self.pol=list(data)
                self.pol.append(data[0])
                self.pol.append(data[1])
            else:
                print("Insert 2 element: base and height")
                self.__del__()

        #calcolo l'area del rettangolo
        #@return: area del rettangolo
        def area(self):
            return self.pol[0]*self.pol[1]


    #creo un rettangolo
    myRect = rectangle((10,20))

    #stampo i 4 lati del rettangolo
    print("Print all side of rect: ")
    myRect.printAll()

    #calcolo l'area del rettangolo
    print(f"\nArea:{myRect.area()}")