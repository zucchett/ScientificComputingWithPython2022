import math
from numpy import linspace
from timeit import timeit

def esercizio1(number, type_n):
    #Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
    #Determine the input type in the function, and pass another argument to choose the output representation.
    number=str(number)
    if number[0:2]=="0x": #E' un hex
        if type_n=="d":
            number=int(number,16)
        elif type_n=="b":
            number=bin(int(number, 16))  
        else:
            print("Errore")
            return

    elif number[0:2]=="0b": #E' un bin
        if type_n=="d":
            number=int(number,2)
        elif type_n=="h":
            number=hex(int(number, 2))  
        else:
            print("Errore")
            return
    else:
        try: #Abbiamo un intero
            number=int(number)
            if type_n=="b":
                number=bin(int(number))
            elif type_n=="h":
                number=hex(int(number))
            else:
                print("Errore")
                return
        except BaseException:
            print("Errore")
            return

    return number

def esercizio2(stringa):
    #Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into 
    #a single precision floating point in decimal representation. Interpret the various bits as sign, 
    #fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.
    stringa=str(stringa)
    s=stringa[0]
    e=stringa[1:9]
    f=stringa[9:]

    #parte relativa al segno
    part1=((-1)**int(s))
    print(part1)

    #parte relativa al decimale
    floating_decimal=int(f,2)
    floating_decimal="1"+str(floating_decimal)
    part2=int(floating_decimal)/10**(len(floating_decimal)-1)

    #parte relativa all'esponente
    e=int(e,2)
    part3=2**(e-127)

    valore=part1*part2*part3

    return valore

def esercizio3():
    def overflow():
        a=1.0
        while True:
            a_prev=a
            a=float(a*2)
            try:
                d=str(bin(int(a)))
            except:
                print(a_prev)
                break

    def underflow():
        a=1.0
        while True:
            a_prev=a
            a=a/1.1
            if float(a)==0:
                print(a_prev)
                break

    overflow()
    underflow()

def esercizio4():
    #Similarly to the previous exercise, write a program to determine the machine precision
    #for floating point numbers.

    #define a new variable by adding an increasingly smaller value and check when the
    #addition starts to have no effect on the number.

    def precision():
        var=1
        var_prev=1
        while var != 0:
            var_prev=var
            var=var/2
        return var_prev
    print(precision())

def esercizio5():
    def quadratic(a,b,c):
        
        A1=-b+math.sqrt(b**2 -4*a*c)
        A2=-b-math.sqrt(b**2 -4*a*c)
        
        x1=(A1)/(2*a)
        x2=(A2)/(2*a)
        
        return x1,x2

    def quadratic_confronto(a,b,c):
        
        A1=-b+math.sqrt(b**2 -4*a*c)
        x1=(A1*A1)/(2*a*A1)
        
        A2=-b-math.sqrt(b**2 -4*a*c)
        x2=(A2)*(A2)/(2*a*A2)

        return x1,x2

    def accurate_quadratic(a,b,c):
        d = b**2-4*a*c 
 
        if d < 0: 
           print('The equation has no real solution')
           return None
        
        elif d == 0: 
           x = (-b)/(2*a) 
           return x
        
        else: 
           x1 = (-b+math.sqrt(d))/(2*a) 
           x2 = (-b-math.sqrt(d))/(2*a) 
           return x1,x2
    
    c1,c2 = quadratic(0.001,1000 ,0.001)
    c3,c4 = quadratic_confronto(0.001,1000 ,0.001)
    print(c1,c2)
    print(c3,c4)
    c5,c6 = accurate_quadratic(0.001,1000 ,0.001)
    print(c5,c6)

    #We obtain the same result in both two functions by using a=c=0.001 and b=1000, in fact:
    print(c1==c3,c2==c4)
    #But if we solve the formula with smaller values of a,b,c (i.e. a=c=0.0001, b=10000) we get a
    #ZeroDivisionError by the second function.

def esercizio6():
    def f(x):
        return x*(x-1)

    def derivative(x_0, delta):
        df=(f(x_0+delta)-f(x_0))/delta
        return df
    a=1 #Valore attorno al quale avviene calcolata la derivata
    
    print(derivative(a,10**(-2)))
    #The numerical and analytical results are different because in the analytical 
    #method we consider a delta smaller than the one that we consider in the numerical method.
    #By using:
    print(derivative(a,10**(-4))) #1.0000999999998899
    print(derivative(a,10**(-6))) #1.0000009999177333
    print(derivative(a,10**(-8))) #1.0000000039225287
    print(derivative(a,10**(-10))) #1.000000082840371
    print(derivative(a,10**(-12))) #1.0000889005833413
    print(derivative(a,10**(-14))) #0.9992007221626509
    print(derivative(a,10**(-15))) #1.1102230246251577
    #The accuracy of df/dx scales linearly until delta get the value 10**(-10).
    #Then, the result get worse and worse, according to the limitations of disctretized numbers

def esercizio7(x=100):
    def f(x):
        return math.sqrt(1-x**2)
    
    def integral(N=100):
        l=linspace(-1,1,N)
        result=0
        for i in range(N):
            result=result+(2/N)*f(l[i])
        return result
    
    #With N=100 the error is: 0.553171569526791%
    print(str(100*(math.pi/2-integral(x))/math.pi)+"%")
    print(timeit(integral,number=1))
    #Dopo alcuni tentativi si puo osservare che il valore di N che verifica la
    #condizione di far durare la computazione 1 secondo è N=1360000, con un errore del:  3.679808518244348e-05%
    return integral(x)

esercizio7()
