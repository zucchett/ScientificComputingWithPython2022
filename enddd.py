#1.1"
a = []
for i in range(1, 100):
    if i%3==0 and i%5==0:
        print("Hello World")  
        a.append("HelloWorld")
        
    elif i%3==0:
        print("Hello")
        a.append("Hello")  
    elif i%5==0:
        print("World")
        a.append("World")  
    else:
        print(i)
        a.append(i)  
print("!!!!!!!!2nd step!!!!!!!")
counter = 0
for i in a:
    if i=="Hello":
        a[counter]="Python"
    
    elif i=="World":
        a[counter]="Works"
    counter = counter +1
def convert(a):
    return tuple(a)
print(convert(a))

#1.2
x = input('choose 1st number')  

y = input('choose 2nd number') 

print ('1st number is:' +y +'  second number is:'+ x)
#1.3
import math

a=(8,0)
b=(0,15)
c=math.sqrt(pow(abs(a[0]-b[0]),2)+pow(abs(a[1]-b[1]),2))
print(c)

#1.4
from collections import Counter

s1 = "Write a program that prints the numbers from 1 to 100.\
But for multiples of three print Hello instead of the number and for the multiples of five print World.\
For numbers which are multiples of both three and five print HelloWorld."

count_s1 = Counter(s1.lower())

print(count_s1)

s2 = "The quick brown fox jumps over the lazy dog"
count_s2 = Counter(s2.lower())
print(count_s2)

#1.5
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20] 

list1 = [] 
 
number_of_uniques = 0
 
for i in l: 
    if i not in list1: 
        number_of_uniques = number_of_uniques + 1
        list1.append(i) 
print("Unique numbers are : ",list1)
print("Total unique numbers are:", number_of_uniques)


#1.6
a = input('can you write something?')  

b = input('please write something again') 

try:
    a = float(a)
    b = float(b)
    d = a +b
    print(d)
except:
    print( " the sum is not a number")

#1.7
l = [0,1,2,3,4,5,6,7,8,9,10] 

list1 = [] 
for i in l:  
    cubes = i**3
    list1.append(cubes) 

print(list1)

cubes2 = [k**3 for k in l]
print(cubes2)


#1.8
numbers= [(i,j) for i in range (0,3) for j in range (0,4)]
print(numbers)


#1.9
import math
list1 = []
for i in range(1,100):
    for j in range(1,100):
        c = math.sqrt(pow(i,2)+pow(j,2))
        if c%1 ==0 and c<100:
            c = int(c)
            list1.append((i,j,c))
list1 = tuple(list1)
print(list1)
        

#1.10
def normalization(vectoor):
    length=[]
    for i in range (len(vectoor)):
        length.append(vectoor[i]*vectoor[i])
    totallength=sum(length)
    vectorlength= totallength**0.5
    for i in range (len(vectoor)):
        length[i]=vectoor[i] / vectorlength
    return length
vector=(6,9,19,99)
print("vector input", vector)
print("the normalizationed value is :" , normalization(vector))

#1.11 
n1=0
n2=1
i=0
while i<20:

    n3= n1+n2
    n1=n2
    n2=n3
    i=i+1
    print (n3)
    
#2.1
def f(x):
    list_f=[]
    for i in range(x):
        list_f.append(i)
    return list_f

alist = [1, 2, 3]
ans = f(5)
print(ans)
print(alist) # alist has been changed

#2.2
desired_values = [x*x for x in range(10) if x % 2 == 1]
print(desired_values)

#2.3
def compare(x):
    if len(x) <= 8:
        return True
    return False

test_list =(["PHP", "Exercises", "Backend", "ww","wwjjjjjjjjjjjsz"])

print(list(filter(compare,  test_list)))


#2.4
def length(x):
    return len(x)
        
        
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

x = list(map(length, lang))
print(x)


#2.5
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x: x[0] )
print(language_scores)


#2.6
def square(x):
    """Square of x."""
    return x * x

def cube(x):
    "cube of x"
    return x*x*x
def sixth(x):
    
    return cube(square(x))
x=2
print (sixth(x))


#2.7
def hello(func):
    def wrapper(*args, **kwargs):
        print ("Hello World")
        func(*args, **kwargs) 
    return wrapper 
@hello
def square(x):
     return x*x


square(8)
square (1)

#2.8
def fibo(ş):
    if ş <= 1:
        return ş
    else:
        return(fibo(ş-1) + fibo(ş-2))

nterms = 20


print("Fibonacci sequence:")
for i in range(nterms):
    print(fibo(i))


#2.9
import timeit

def loopFibonaci(x):
    n1=0
    n2=1
    i=0
    while i<x:
        n3= n1+n2
        n1=n2
        n2=n3
        i=i+1
        print (n3)
    
    
def recursiveFibonaci(ş):
    if ş <= 1:
        return ş
    else:
        return(fibo(ş-1) + fibo(ş-2))
print("Fibonacci sequence:")
for i in range(nterms):
    print(fibo(i))

    
beginning1=timeit.default_timer()
print("start time is :" , beginning1, "for loop fibonacci")
loopFibonaci(20)
print ("the differences between times are", timeit.default_timer()-beginning1)

beginning2=timeit.default_timer()
print("start time is :" , beginning2, "recursiveFibonaci")
recursiveFibonaci(20)
print ("the differences between times are", timeit.default_timer()-beginning2)

#according to calculations,loop is more efficent than recucrsive 


#2.10
import math

class polygon:
    x = []
    def __init__(self, components):
        self.x = components
    
    def perimeter(self):
        return sum(self.x)
    def getOrderedSides(self=True):
        return sorted(self.x)
    
sides = []    
a= int(input("please enter the number of sides"))
for i in range(a):
    temp = int(input("please enter the length of side"))
    sides.append(temp)
pol = polygon(sides)

sides= tuple(sides)

print(pol.perimeter())
a=pol.getOrderedSides()
a= tuple(a)
print(a)


class rectangle(polygon): 
    x = []
    def __init__(self, x):
        if (a) == 4 and ((x[1]==x[2] and x[3]==x[0])or(x[1]==x[3] and x[2]==x[0])or (x[1]==x[0] and x[3]==x[2])):
            self.x = x 
            
        else:
            print("Error: number of components is not 4")
    
    
    def area(self,x):
        
        if (sides[1]==sides[2]) :
            c=int(sides[1])*int(sides[3])
            return ("total area of rectangular is",c)
        elif (sides[1]==sides[3]):
            d = int(sides[1])*sides([2])
            return ("total area of rectangular is",d)
        elif (sides[1]==sides[0]):
            e= sides[1]*sides[3]
            return ("total area of rectangular is",e)
        
sides = []    
a= int(input("please enter a value"))
for i in range(a):
    temp = int(input("please enter side"))
    sides.append(temp)

rec = rectangle(sides)

rec1 = rec.area(x)


print(rec1)
b=rec.getOrderedSides()
b= tuple(b)
print(b)

#3.1

a= (input("please enter a value"))
if a[1]==("b"):
    print("your variable type is binary")
    dec= int(a,2)
    hexa= hex(dec)
    
    c= (input("please write which type you want to convert write (write h for hexadecimal, d for decimal)"))
    if c[0]== ("d"):
        print(dec)
    if c[0]==("h"):
        print(hexa)
    
    
elif a[1]==("x"):
    print("your variable type is hexadecimal")
    dec= int(a,16)
    binn= bin(dec)
    
    c= (input("please write which type you want to convert write (write b for binary, d for decimal)"))
    if c[0]== ("d"):
        print(dec)
    if c[0]==("b"):
        print(binn)
    
else:
    print("your variable type is decimal")
    binn= bin(int(a))
    hexa= hex(int(a))
    
    c= (input("please write which type you want to convert write (write h for binary b, h for hexadecimal)"))
    if c[0]== ("b"):
        print(binn)
    if c[0]==("h"):
        print(hexa)

#3.2
import math

def sprecision(numberF):
    numberF=list(numberF)
    count=0
    result=0
    exponent = 0
    
    
    for a in numberF[8:31]:
        result = (int(a)/(pow(2,count))+ result )
        count +=1
    count = 7
    
    for a in numberF[1:9]:
        exponent = + (int(a)*pow(2,count)+exponent )
        count-=count
        
    result =result * pow(2,(exponent-127)) 
    if numberF[0] == 0:
        print(result)
    else:
        print(-result)
        
x = "11000000101100000000000000000000"
sprecision(x)

#3.3
A=5000
underf=1
overf=1
factor=2
for n in range (A):
    underf=underf/2
    print("%2d"%n, "2.5%e"%underf)
    if underf==0:
        print("it's the last points for underflow ")
        break
for n in range (A):
    try:
        overf=overf*2
        
        print("%2d"%n,"2.5%e"%overf)  
    except:
        print("it's the last points for overflow")
        break




#3.4
A=60
underf=0.5
underf1=0
k=0
for n in range (A):
    underf1=underf*pow(2,-n)
    if underf1==0and k==0: 
        print("after",n,"th iteration there won't be any contribution and function returns 0 after that point")
        k=k+1
    underf=underf1
    print (underf1)
    
    
#3.5
import math
def calculation(a,b,c):
    x1= ((-b+math.sqrt(b**2-4*a*c))/(2*a))
    x2= ((-b-math.sqrt(b**2-4*a*c))/(2*a))
    
    funcvalue1=a*x1**2+b*x1+c
    funcvalue2=a*x2**2+b*x2+c
    average_error=(funcvalue1+funcvalue2)/2

    return x1,x2,"average error is",average_error

def calculation2(a,b,c):
    x11= ((-b+math.sqrt(b**2-4*a*c))*(-b-math.sqrt(b**2-4*a*c))/((2*a)*(-b-math.sqrt(b**2-4*a*c))))
    x22= ((-b-math.sqrt(b**2-4*a*c))*(-b+math.sqrt(b**2-4*a*c))/((2*a)*(-b+math.sqrt(b**2-4*a*c))))
    x33= ((-b+math.sqrt(b**2-4*a*c))*(-b+math.sqrt(b**2-4*a*c))/((2*a)*(-b-math.sqrt(b**2-4*a*c))))
    x44= ((-b-math.sqrt(b**2-4*a*c))*(-b-math.sqrt(b**2-4*a*c))/((2*a)*(-b+math.sqrt(b**2-4*a*c))))
 
    
    funcvalue11=a*x11**2+b*x11+c
    funcvalue22=a*x22**2+b*x22+c
    funcvalue33=a*x33**2+b*x33+c
    funcvalue44=a*x44**2+b*x44+c
    average_error2=(funcvalue11+funcvalue22+funcvalue33+funcvalue44)/4

    return x11,x22,x33,x44,"average error is",average_error2

   
print(calculation(0.001,1000,0.001))
print(calculation2(0.001,1000,0.001))



#According to calculations there aren't differences between x1 and x11 roots.
#However 2nd calculation I found 4 roots. 
#In the 1st calculation, average error is 4.1527324856193565e-08 and 2nd calculation 2.500052877829632e+32. 
#Since the second error is less than 1st one, 2nd solution is better.


def calculatiooon(a,b,c):
    delta=(b**2-4*a*c)
    if delta==0:
        return((-b/(2*a)),(-b/(2*a)))
    elif delta>0:
        x1= ((-b+(delta**(0.5)))/(2*a))
        x2= ((-b-(delta**(0.5)))/(2*a))
        return (x1,x2)
    else:
        reelp=(-b/(2*a))
        imaginaryp=(delta**0.5)/(2*a)
        print (reelp,"+", imaginaryp,"i")
        print (reelp,"-", imaginaryp,"i")

equationa= (input("please write your a value in function in a*x**2+b*x+c format"))
equationb= (input("please write your b value in function in a*x**2+b*x+c format"))
equationc= (input("please write your c value in function in a*x**2+b*x+c format"))

a=float(equationa)
b=float(equationb)
c=float(equationc)


print(calculatiooon(a,b,c))


#3.6
def f(x):
    return x*(x-1)
def der(x,delta):
    result=(f(x+delta)-f(x))/delta
    return result
x=1
delta1=10**-2
delta2=10**-4
delta3=10**-6
delta4=10**-8
delta5=10**-10
delta6=10**-12
delta7=10**-14
print(x,'is your x')
print ("result while delta is equal to:",delta1,"-------" , der(x,delta1))
print ("result while delta is equal to:",delta2,"-------" , der(x,delta2))
print ("result while delta is equal to:",delta3,"-------" , der(x,delta3))
print ("result while delta is equal to:",delta4,"-------" , der(x,delta4))
print ("result while delta is equal to:",delta5,"-------" , der(x,delta5))
print ("result while delta is equal to:",delta6,"-------" , der(x,delta6))
print ("result while delta is equal to:",delta7,"-------" , der(x,delta7))
# until delta is equal to 10**8 accuracy will increase. However, after that point function diverse to 0.

#3.7
import math
import timeit
def rieemann(N):
    summ=0
    for i in range (N):
        x= ((1/N)*i)-1
        summ= summ+(1/N)*((1-x**2)**0.5)
    summ = summ * 2
    return summ
pat=rieemann(100)
print("while N is equal to 100", pat,"obtained error is" , ((math.pi/2)-pat))
    
beginning = timeit.default_timer()
print("The start time is :",beginning)

result = rieemann(189999999)
print("Erorr: ", result, "N: 999", "Result: ", (math.pi/2 - result))


print("The time difference is :", timeit.default_timer() - beginning) 
