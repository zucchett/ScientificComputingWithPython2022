# 01ex
#Author: Riccardo Mosele 2044736
import math
from nis import match
import re

printEs1=False
printEs2=False
printEs3=False
printEs4=False
printEs5=False
printEs6=False
printEs7=False
printEs8=False
printEs9=False
printEs10=False
printEs11=False


#***************************************************Ex 1.1
if(printEs1):

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
    x = input('insert X: ')
    y = input('insert Y: ')

    x, y = y, x
    print("x =", x)
    print("y =", y)

#***************************************************Ex 1.3
if(printEs3):

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
    def countingLetters(m):

        print("STRINGA:\n"+m+"\n")

        s = m.lower()   

        print("a: "+str(s.count('a')))
        print("b: "+str(s.count('b')))
        print("c: "+str(s.count('c')))
        print("d: "+str(s.count('d')))
        print("e: "+str(s.count('e')))
        print("f: "+str(s.count('f')))
        print("g: "+str(s.count('g')))
        print("h: "+str(s.count('h')))
        print("i: "+str(s.count('i')))
        print("j: "+str(s.count('j')))
        print("k: "+str(s.count('k')))
        print("l: "+str(s.count('l')))
        print("m: "+str(s.count('m')))
        print("n: "+str(s.count('n')))
        print("o: "+str(s.count('o')))
        print("p: "+str(s.count('p')))
        print("q: "+str(s.count('q')))
        print("r: "+str(s.count('r')))
        print("s: "+str(s.count('s')))
        print("t: "+str(s.count('t')))
        print("u: "+str(s.count('u')))
        print("v: "+str(s.count('v')))
        print("w: "+str(s.count('w')))
        print("x: "+str(s.count('x')))
        print("y: "+str(s.count('y')))
        print("z: "+str(s.count('z')))


    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers Which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"
    s3 = "aaaabbbb cccc dd"

    countingLetters(s1)

#***************************************************Ex 1.5
if(printEs5):

    def get_unique_numbers(numbers):
        unique_list = []

        for i in numbers:
            if i in unique_list:

                continue
            else:
                unique_list.append(i)
        return unique_list

    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
    85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
    1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
    45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
    
    unique_numbers = list(set(l))
    print("With Set:")
    print(unique_numbers)

    print("With Other:")
    res=get_unique_numbers(l)
    res.sort()
    print(res)

    print("unique numbers are: "+str(len(res))+" of "+str(len(l)))

#***************************************************Ex 1.6

#***************************************************Ex 1.7

#***************************************************Ex 1.8

#***************************************************Ex 1.9

#***************************************************Ex 1.10

#***************************************************Ex 1.11


