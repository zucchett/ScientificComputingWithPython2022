#esercizio1
print("##########EX1##########")
temp=[]
for i in range (100): ##conditions to print
	j=i+1
	if (j%3==0 and j%5==0):
		print("Hello World")
		temp.append("Hello World")
	elif (j%5==0):
		print("World")
		temp.append("World")
	elif (j%3==0):
		print("Hello")
		temp.append("Hello")
	else:
		print(j)
		temp.append(j)

definitive = tuple (temp) ##cast to a tuple
for x in range (len(temp)):
	if (temp[x]== "Hello"):
		temp[x]= "Python"
	if (temp[x]== "World"):
		temp[x]= "Works"
definitive_2= tuple (temp)
print (definitive_2)

#esercizio2
print("##########EX2##########")

x=input("Inserisci x:")
y=input("Inserisci y:")
x,y=y,x ##using python sintax to switch the content of the variables
print("x ora vale",x,"y  ora vale",y)

#esercizio3
print("##########EX3##########")
import math ##importing math module for square root function
u=(5,6)
v=(80,90)
dist=math.sqrt(((u[0]-v[0])**2)+((u[1]-v[1])**2)) ##computing the distance
print ("La distanza tra questi punti è",dist)
#esercizio4
print("##########EX4##########")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1=s1.upper() ##ignoring the lower/upper case
s2=s2.upper() ##ignoring the lower/upper case
occur=[] ##empty lists
occur_2=[] 
for char in s1:
	count=s1.count(char)
	occur.append((count,char)) ##counting the occurrences
for char in s2:
	count=s2.count(char)
	occur_2.append((count,char))  ##counting the occurrences
print("L'occorrenza nella prima stringa è",occur)
print("L'occorrenza nella seconda stringa è",occur_2)
#esercizio5
print("##########EX5##########")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique = set() ##using the set to exclude duplicate elements
count = [] 
cont=0
for element in l:
	
	unique.add(element)

for x in unique:
	cont=cont+1 ##counting unique elements

print("I numeri unici sono", cont)
print(unique)

#esercizio6
print("##########EX6##########")
p=input("Inserisci un numero:")
q=input("Inserisci un'altro numero:")
try:
	q=float (q) ##summing the two numbers casting them to float
	p=float (p) 
	z=p+q
	print("La somma di quei due numeri è",z)
except:
	print("Addizione non possibile") ##if the addition returns an error, print the message
##esercizio7
print("##########EX7##########")
cubes = []

for i in range(11):

	cubes.append(i**3)  ##for cycle

cubes2=[x**3 for x in range(11)] ##list comprehension

print(cubes)
print(cubes2)

##esercizio8
print("##########EX8##########")
b=[(i,j) for i in range(3) for j in range(4)]
print(b)
##esercizio9
print("##########EX9##########")
l=[]  	##empty list
limite=99
c=0
m=2
while(c<limite):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limite):		##algorithm to determine the triple
            break
        if(a==0 or b==0 or c==0):
            break
        l.append((a,b,c)) 	##appending the triple to the list
    m=m+1
def_tuple= tuple(l) ##casting to tuple
print(def_tuple)
##esercizio10
print("##########EX10##########")
norm=0
somma=0
numbers=[7,32,48,55,66,34,22,325]	##list of the numbers
for x in numbers:
	norm= norm+ x**2	##calculating the sum of the squares
norm=math.sqrt(norm)
for i in range(len(numbers)):
	numbers[i]=numbers[i]/norm	##normalizing the elements
	somma=somma+numbers[i]**2	##checking their sum



print("I numeri normalizzati sono",numbers)
print("Difatti, la somma dei loro quadrati è",somma)

##es11
print("##########EX11##########")
fib=[0,1] ##default case
while len(fib)<20:
	fib.append(fib[len(fib)-1]+fib[len(fib)-2])	##calculating other elements of the Fibonacci sequence

print("La sequenza di fibonacci desiderata è",fib)



	

