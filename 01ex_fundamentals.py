#ESERCIZIO 1
print('\n'+'_________ESERCIZIO_1__________')
i=0
l=[]
while i<100:
    i=i+1
    if i%3==0 and i%5==0:
        print("HelloWorld")
        l.append("HelloWorld")
    elif i%3==0:
            print("Hello")
            l.append("Hello")
    elif i%5==0:
            print("World")
            l.append("World")
    else:
        print(i)
        l.append(i)
j=0;
for x in l:
    if x=="Hello":
        l[j]="Python"
    elif x=="World":
        l[j]="Works"
    j=j+1

t=tuple(l)
print(t)





#ESERCIZIO 2
print('\n'+'_________ESERCIZIO_2__________')
x=input('Type x: ')
y=input('Type y: ')
x,y = y,x
print('x='+str(x))
print('y='+str(y))




#ESERCIZIO 3
print('\n'+'_________ESERCIZIO_3__________')
import math
def euc_distance(u,v):
    return math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
u=(3,0)
v=(0,4)
print(euc_distance(u,v))




#ESERCIZIO 4
print('\n'+'_________ESERCIZIO_4__________')
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number>s2 = "The quick brown fox jumps over the lazy dog"

a={}
j=0
for x in s1:
    try:
        count=a[s1[j].lower()]
    except:
        count=0
    a.update({s1[j].lower():count+1})
    j=j+1
print(a)

b={}
j=0
for x in s2:
    try:
        count=b[s2[j].lower()]
    except:
        count=0
    b.update({s2[j].lower():count+1})
    j=j+1
print(b)

#ESERCIZIO 5
print('\n'+'_________ESERCIZIO_5__________')
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
a_dict={}
j=0
for x in l:
    try:
        count=a_dict[l[j]]
    except:
        count=0
    a_dict.update({l[j]:count+1})
    j=j+1

for k in a_dict.keys():
    if a_dict[k]>1:
        count=a_dict[k]
        while count>0:
            l.remove(k)
            count-=1

print(l)
print('Counts of unique numbers: '+str(len(l)))




#ESERCIZIO 6
print('\n'+'_________ESERCIZIO_6__________')
var1=input('Type var1: ')
var2=input('Type var2: ')
try:
    sum= float(var1)+float(var2)
    print(sum)
except:
    print("Addition not possible")

#ESERCIZIO 7
print('\n'+'_________ESERCIZIO_7__________')
l=[]
for i in range(11):
        l.append(i**3)
print(l)

new_l=[x**3 for x in range(11)]
print(new_l)





#ESERCIZIO 8
print('\n'+'_________ESERCIZIO_8__________')
b=range(3)
c=range(4)
d=[(x,y) for x in b for y in c]
print(d)





#ESERCIZIO 9
print('\n'+'_________ESERCIZIO_9__________')
import math
t=[(a,b,c) for a in range(1,100) for b in range(a,100) for c in range(b,100) if a**2+b**2==c**2 and a+b>c]
print(t)


#ESERCIZIO 10
print('\n'+'_________ESERCIZIO_10__________')
t=(1,2,3,4)

import math
l=[]
den=0
for i in range(len(t)):
    den+=t[i]**2
den=math.sqrt(den)
for i in range(len(t)):
    l.append(t[i]/den)
print(l)





#ESERCIZIO 11
print('\n'+'_________ESERCIZIO_11__________')
l=[1,1]
i=2
while i<20:
    l.append(l[i-2]+l[i-1])
    i+=1
print(l)
