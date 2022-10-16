#Ex 1
print("Exercise 1")
out_tuple = ()

for i in [x+1 for x in range(100)]:
    if i%15 == 0:
        
        out_tuple = out_tuple + ('Hello World',)
        print('Hello World')
    elif i%5 == 0:
        out_tuple = out_tuple + ('Works',)
        print('World')
    elif i%3 == 0:
        out_tuple = out_tuple + ('Python',)
        print('Hello')
    else:
        out_tuple = out_tuple + (i,)
        print(i)




print(out_tuple)

#Ex 2
print("Exercise 2")

#a = input("Enter x and y values separated by a space: ").split()        ATTENTO SISTEMA QUA
a = [0, 1]
a.reverse()
print(a[0],a[1]) 

#Ex 3
print("Exercise 3")

import math

def euclideanDistance(p1, p2):
    print("The distance between these two points is: ")
    print(math.sqrt(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2)))

p1 = (3,0)
p2 = (0,4)

euclideanDistance(p1,p2)


#Ex 4
print("Exercise 4")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


s1 = s1.lower()
s2 = s2.lower() 

char_in_s1 = {}
for i in s1:
    if i in char_in_s1:
        char_in_s1[i] = char_in_s1[i] +1
    else:
        char_in_s1[i] = 1


char_in_s2 = {}
for i in s2:
    if i in char_in_s2:
        char_in_s2[i] = char_in_s2[i] +1
    else:
        char_in_s2[i] = 1

print(char_in_s1)
print(char_in_s2)


#Es 5
print("Exercise 5")


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

out_num = []

for i in l:
    found = False
    for j in range(len(out_num)):
        if i == out_num[j]:
            found = True
    if not found:
        out_num.append(i)


out_num.sort()
print(out_num)



out_using_set = set()


for i in l:
    out_using_set.add(i)

print(out_using_set)


#Es 6
print("Exercise 6")

a = input("Insert first value ")
b = input("Insert second value ")

try:
    a = float(a)
    b = float(b)
    if (a+b)%1==0:
        print(int(a+b))
    else: print(a+b)
except:
    a = str(a)
    b = str(b)
    print(a+' '+b)


