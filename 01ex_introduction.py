# 01ex
#Author: Riccardo Mosele 2044736
import math
from nis import match
import re

printEs1=False
printEs2=False
printEs3=False
printEs4=True
printEs5=False
printEs6=False
printEs7=False
printEs8=False
printEs9=False
printEs10=False
printEs11=False


#***************************************************Ex 1.1
if(printEs1):
    print("***************************************************Ex 1.1")
    listaTest=[]
    for x in range(1,101,1):
        if (x%3==0 and x%5==0):
            listaTest.append("HelloWorld")
            #print("HelloWorld")
    
        elif x%3==0:
            listaTest.append("Hello")
            #print("Hello")

        elif x%5==0:
            listaTest.append("World")
            #print("World")

        else: 
            listaTest.append(x)
            #print(x) 

    for i in range(len(listaTest)):
        if (listaTest[i]=="Hello"):
            listaTest[i]="Python"
        elif (listaTest[i]=="World"):
            listaTest[i]="Works"

    tuplaResut = (tuple(listaTest))
    print(tuplaResut)

#***************************************************Ex 1.2
if(printEs2):
    print("***************************************************Ex 1.2")
    x = input('insert X: ')
    y = input('insert Y: ')

    x, y = y, x
    print("x =", x)
    print("y =", y)

#***************************************************Ex 1.3
if(printEs3):
    print("***************************************************Ex 1.3")
    def computingDistance(u,v):
        return math.sqrt((v[0]-u[0])**2+((v[1]-u[1]))**2)
    
    x1 = input('insert x1: ')
    y1 = input('insert y1: ')
    x2 = input('insert x2: ')
    y2 = input('insert y2: ')
    u=(int(x1),int(y1))
    v=(int(x2),int(y2))
    res = computingDistance(u,v)
    print(res)

#***************************************************Ex 1.4
if(printEs4):
    print("***************************************************Ex 1.4")
    def countingLetters(m):

        print("STRINGA:\n"+m+"\n")

        s = m.lower() 
        occ={}  

        for char in s:
            occ[char]=s.count(char)
        print(f"Occurs: {occ}")

        
    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers Which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"
    s3 = "aaaabbbb cccc dd"

    countingLetters(s1)

#***************************************************Ex 1.5
if(printEs5):
    print("***************************************************Ex 1.5")

    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
    85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
    1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
    45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
    
    #unique_numbers = list(set(l))
    #print("With Set:")
    #print(unique_numbers)
    #print("unique numbers are: "+str(len(unique_numbers)))

    unique_numbers = {}
    not_unique_numbers={}

    for i in l:
        if not i in not_unique_numbers:
            if l.count(i) == 1:
                unique_numbers[i] = l.count(i)
            else:
                not_unique_numbers[i] = l.count(i)
    print("Unique numbers are: " +str(len(unique_numbers)))
    print(unique_numbers)
    
#***************************************************Ex 1.6
if(printEs6):
    print("***************************************************Ex 1.6")

    x = input("Please enter first integer, float or string value: ")
    y = input("Please enter second integer, float or string value: ")
    
    try:
        res=float(x)+float(y)
        print(res)
    except:
        print("ERROR: Sum is not possible!")
   
#***************************************************Ex 1.7
if(printEs7):
    print("***************************************************Ex 1.7")
    listCubicLoop=[]
    for i in range(10):
        listCubicLoop.append(i**3)
    print("With loop:\n"+str(listCubicLoop))

    listCubicCompr = [i**3 for i in range(10)]
    print("With comprehension:\n"+str(listCubicCompr))

#***************************************************Ex 1.8
if(printEs8):
    print("***************************************************Ex 1.8")
    a = []
    for i in range(3):
        for j in range(4):
            a.append((i, j))
    print("With for:\n"+str(a))

    a_compr = [(x, y) for x in range(3) for y in range(4)]
    print("With list comprehension:\n"+str(a_compr))

#***************************************************Ex 1.9
if(printEs9):
    print("***************************************************Ex 1.9")

    listPy=[]
    c, m = 0, 2
 
    while c < 99 :
        
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > 99 :
                break

            listPy.append((a,b,c))
 
        m = m + 1
    
    tuplaPy = (tuple(listPy))
    print(tuplaPy)

#***************************************************Ex 1.10
if(printEs10):
    print("***************************************************Ex 1.10")

    numbers=[5,16,458,102,27,65,31,2,48,124,57]
    print("Original numbers:\n"+str(numbers))
    norm=0

    for i in numbers:
        norm = norm + i**2

    norm = math.sqrt(norm)

    for n in range(len(numbers)):
        numbers[n] = numbers[n]/norm
    
    print("Normalize numbers:\n"+str(numbers))

    sum=0
    for s in range(len(numbers)):
        sum = sum+numbers[s]**2
    print("The sum of the normalized number are:\n"+str(sum))

#***************************************************Ex 1.11
if(printEs11):
    print("***************************************************Ex 1.11")

    fibSeq=[1,1]

    for i in range(20):
        fibSeq.append(fibSeq[len(fibSeq)-1]+fibSeq[len(fibSeq)-2])
    print("First 20 numbers of the Fibonacci sequence:\n"+str(fibSeq))
