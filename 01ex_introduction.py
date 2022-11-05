# Cecilia Rossi      mat. 2091484
###################  01 EX INTRODUCTION ####################################

####### Exercise 1

lista = list()
for i in range(100):
    i += 1
    res = ''
    if i % 3 == 0:
        res += 'Hello'
    if i % 5 == 0:
        res += 'World'
    if i % 3 != 0 and i % 5 != 0:
        print(i)
        lista.append(i)
        continue
    print(res)
    lista.append(res)

lista_b = lista[:]
for k in range(100):
    el = lista_b[k]
    if isinstance(el,int):
        continue
    else:
        lista_b[k] = el.replace('Hello','Python')
        lista_b[k] = lista_b[k].replace('World','Works')
        
tupla = tuple(lista_b)
print(tupla)

####### Exercise 2

x = input('Inserire il valore della prima variabile: ')
y = input('Inserire il valore della seconda variabile: ')
(x,y) = (y,x)
print(x)
print(y)

####### Exercise 3

import math

def distance(u,v):
    d = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
    return d

u = (3,0)
v = (0,4)
distance(u,v)

####### Exercise 4

def letterCount(s):
    counts = dict()
    for car in s.upper():
        if car not in counts:
            counts[car] = 1
        else:
            counts[car] += 1
    return counts

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

counts1 = letterCount(s1)
print(counts1)
counts2 = letterCount(s2)
print(counts2)

####### Exercise 5

#a)
def findUniques(lista):
    uniques = list()
    for i in range(len(lista)):
        car = lista[i]
        lista_new = lista[:]
        lista_new[i] = ''
        if car not in lista_new:
            uniques.append(car)
    return (uniques)

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
uniques = findUniques(l)
print(uniques, len(uniques))

#b)
def findOccurrences(lista):
    counts = dict()
    for car in lista:
        if car not in counts:
            counts[car] = 1
        else:
            counts[car] += 1
    return counts

counts = findOccurrences(l)
uniques2 = list()
for key in counts:
    if counts[key] == 1:
        uniques2.append(key)
print(uniques2, len(uniques2))

####### Exercise 6

x = input('Inserire la prima variabile (int, float o str): ')
y = input('Inserire la seconda variabile (int, float o str): ')

try: #x è un intero o float
    x = float(x)
    try: #anche y è un numero
        y = float(y)
        res = x + y
        if res % 1 == 0:
            res = int(res) #lo converto in intero (se sia x che y sono interi), altrimenti rimane float
        print('Il risultato è:', res)
    except: #y è una stringa
        print("Non è possibile eseguire l'operazione tra le due variabili") #x numero e y stringa
except: #x è una stringa
    try: 
        y = float(y) 
        print("Non è possibile eseguire l'operazione tra le due variabili")
    except: #anche y è una stringa
            res = x+y
            print('Il risultato è:', res)

####### Exercise 7

#Using only a List Comprehension and a for lopp
cubes = []
cubes.append('')

for i in range(10):
    i += 1
    cubo = [['x' for k in range (i)] for k in range(i)]
    cubes.append(cubo)

#Stampo i risultati
for k in cubes:
    print(k,'\n')

####### Exercise 8

print([(i,j) for i in range(3) for j in range(4)])

####### Exercise 9

import math
pythagorean = tuple([(a, b, int(math.sqrt(a**2 + b**2))) for a in range(100) for b in range(100) if a != 0 and b!= 0 and math.sqrt(a**2 + b**2) % 1 == 0 and math.sqrt(a**2 + b**2) < 100])
print(pythagorean)

####### Exercise 10

tupla = (2,1,3)
quadr = [x**2 for x in tupla]
norma = math.sqrt(sum(quadr))
tupla_norm = tuple([x/norma for x in tupla])
print(tupla_norm)
#verifico
print(math.sqrt(sum([x**2 for x in tupla_norm])))

####### Exercise 11

fibonacci = list()
for i in range(20):
    if i == 0 or i == 1:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
print(fibonacci)
