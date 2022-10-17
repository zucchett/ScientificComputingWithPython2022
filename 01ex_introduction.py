#esercizio1

temp=[]

for i in range (100):
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

definitive = tuple (temp)
for x in range (len(temp)):
	if (temp[x]== "Hello"):
		temp[x]= "Python"
	if (temp[x]== "World"):
		temp[x]= "Works"
definitive_2= tuple (temp)


#esercizio2
print (definitive_2)

x=input("Inserisci x:")
y=input("Inserisci y:")
x,y=y,x
print(x,y)

#esercizio3
import math
u=(5,6)
v=(80,90)
dist=math.sqrt(((u[0]-v[0])**2)+((u[1]-v[1])**2))
print (dist)
#esercizio4
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1=s1.upper()
s2=s2.upper()
occur=[]
occur_2=[]
for char in s1:
	count=s1.count(char)
	occur.append((count,char))
for char in s2:
	count=s2.count(char)
	occur_2.append((count,char))

print(occur_2)
#esercizio5
unique=[]
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
for x in l:
	if x not in unique:
		unique.append(x)

print(unique)

#esercizio6
p=input("Inserisci qualcosa:")
q=input("Inserisci qualcos'altro:")
try:
	q=float (q)
	p=float (p)
	z=p+q
	print(z)
except:
	print("Addizione non possibile")
##esercizio7
cubes=[x**3 for i in range (11)]
cubes_2=[]
for i in range (11):
	cubes_2.append(i**3)
##esercizio8
b=[(i,j) for i in range(3) for j in range(4)]
print(b)
##esercizio9
l=[]
limite=99
c=0
m=2
while(c<limite):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limite):
            break
        if(a==0 or b==0 or c==0):
            break
        l.append((a,b,c))
    m=m+1
def_tuple= tuple(l)
print(def_tuple)
##esercizio10
norm=0
somma=0
numbers=[7,32,48,55,66,34,22,325]
for x in numbers:
	norm= norm+ x**2
norm=math.sqrt(norm)
for i in range(len(numbers)):
	numbers[i]=numbers[i]/norm
	somma=somma+numbers[i]**2


print(somma)
print(numbers)

##es10
fib=[0,1]
while len(fib)<20:
	fib.append(fib[len(fib)-1]+fib[len(fib)-2])

print(fib)



	

