def esercizio_1():
    #1. The HelloWorld replacement
    #Write a program that:
    #prints the numbers from 1 to 100 but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
    #for numbers which are multiples of both three and five print "HelloWorld".
    #b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".

    lista=[];
    for i in range(1,100):
        if i%3==0 and i%5==0:
            print("HelloWorld");
            lista.append("PythonWorks");
        elif i%3==0:
            print("Hello");
            lista.append("Python");
        elif i%5==0:
            print("World");
            lista.append("Works");
        else:
            print(i);
            lista.append(i);

    lista=tuple(k for k in lista);
    print(type(lista))

def esercizio_2():
    #2 The swap
    #Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
    #Try to do that without using a temporary variable, exploiting the Python syntax.

    x=int(input("insert number 1:"));
    y=int(input("insert number 2:"));
    x = x+y;
    y= x-y;
    x =x-y;
    print("number 1 now is"+str(x));
    print("number 2 now is"+str(y));

def esercizio_3():
    #3 Computing the distance
    #Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, 
    # where *u* and *v* are both 2-tuples *(x,y)*.
    #Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.

    #*Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.
    from math import sqrt

    x_1=int(input("number 1, coordinate 1"));
    x_2=int(input("number 1, coordinate 2"));

    y_1=int(input("number 2, coordinate 1"));
    y_2=int(input("number 2, coordinate 2"));

    Dist=sqrt((y_1-x_1)**2 + (y_2-x_2)**2);

    print(Dist);

def esercizio_4():
    #4. Counting letters
    #Write a program that calculates the number of times each character occurs in a given string. 
    #Ignore differences in capitalization.
    #The strings are in the cell below.

    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    s1=s1.lower();
    lista=[];
    for i in range(0,len(s1)):
        if s1[i] in lista:
            pass
        else:
            s1.count(s1[i]);
            lista.append(s1[i]);
            print(s1[i]+str(s1.count(s1[i])));
    s2=s2.lower();
    lista=[];
    for i in range(0,len(s2)):
        if s2[i] in lista:
            pass
        else:
            s2.count(s2[i]);
            lista.append(s1[i]);
            print(s2[i]+str(s2.count(s2[i])));
def esercizio_5():
    #Isolating the unique
    #Write a program that determines and counts the unique numbers in the list:

    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
    85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
    1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
    45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20];

    lunghezza=len(l);
    lista_unici=[]
    for i in range(0,lunghezza-1):
        if l.count(l[i])==1:
            lista_unici.append(l[i]);
        else:
            pass
    print(lista_unici);
    print(len(lista_unici));

def esercizio_6():
    #6. Casting
    #Write a program that:
    #reads from command line two variables, that can be either int, float, or str.
    #use the try/except expressions to perform the addition of these two variables, only if possible
    #and print the result without making the code crash for all the int/float/str input combinations.

    value_1=input("value 1:");
    value_2=input("value 2:");

    try:
        float_value1=float(value_1);
        float_value2=float(value_2);
        print(float_value1+float_value2);
        print("Stampa tra float");
    except:
        pass
    try:
        int_value1=int(value_1);
        int_value2=int(value_2);
        print(int_value1+int_value2);
        print("Stampa tra int");
    except:
        pass
    try:
        print(value_1+value_2);
        print("Stampa tra stringhe");
    except:
        pass

def esercizio_7():
    #7. Cubes
    #Create a list of the cubes of x for x in [0, 10] using:
    #a) a for loop
    #b) a list comprehension

    #Method 1
    lista=[]
    for i in range(0,10):
        lista.append([]);
        for k in range(0,i):
            lista[i].append("x"*i);
    for i in range(0,10):
        for k in range(0,i):
            print(str(lista[i][k]));
    #Method 2
    lista=[]
    for i in range(0,10):
        lista.append(["x"*i for k in range(0,i)]);

    for i in range(0,10):
        for k in range(0,i):
            print(str(lista[i][k]));

def esercizio_8():
    #8. List comprehension
    #Write, using the list comprehension, a single-line expression that gets the 
    # same result as the code in the cell below.

    a = [];
    for i in range(3):
        for j in range(4):
            a.append((i, j))
    print(a)

    b=[];
    b=[(i,j) for i in range(3) for j in range(4)];
    print(b);

def esercizio_9():
    #9. Nested list comprehension

    #A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎^2+𝑏^2=𝑐^2 . 
    # The first Pythagorean triple is (3, 4, 5).

    #Find and put in a tuple all unique Pythagorean triples for the positive integers 𝑎
    # ,𝑏  and 𝑐 with 𝑐<100 .
    from math import sqrt
    lista=[];
    #viene scelto 100 come estremo superiore per a e b in prima istanza.
    #Successivamente viene fatta una cernita con le terne che rispettano la condizione.
    for a in range(1,100):
        for b in range(1,100):
            c=sqrt(a**2 + b**2);
            if c==int(c) and c<100 and [b,a,int(c)] not in lista:
                lista.append([a,b,int(c)]);
    lista=tuple(k for k in lista);
    print(lista);
    print(len(lista));

def esercizio_10():
    #10. Normalization of a N-dimensional vector
    #Write a program that takes an N-dimensional vector, 
    #e.g. a variable-length tuple of numbers, and normalizes it to one 
    #(in such a way that the squared sum of all the entries is equal to 1).
    import math
    print("inserire i valori con la forma (x1,x2,..,xn)")
    a=input("Inserire il vettore");
    a=list(a);
    listavalori=[];
    for i in range(0,len(a)-1):
        try:
            valore=int(a[i]);
            listavalori.append(valore);
        except:
            pass
    somma=0;
    for k in range(0,len(listavalori)):#calcolo norma
        somma=somma+listavalori[k]**2;
    somma=math.sqrt(somma);
    for k in range(0,len(listavalori)):
        listavalori[k]=listavalori[k]/somma;
    print(listavalori);
    
def esercizio_11():
    #11 The Fibonacci sequence
    #Calculate the first 20 numbers of the Fibonacci sequence using only `for` 
    # or `while` loops.
    a=0;
    print(a);
    b=1;
    print(b);
    for i in range(0,18):
        c=a+b;
        a=b;
        b=c;
        print(c);


###########TEST SECTION#############
#esercizio_1();
#esercizio_2();
#esercizio_3();
#esercizio_4();
#esercizio_5();
#esercizio_6();
#esercizio_7();
#esercizio_8();
#esercizio_9();
#esercizio_10();
#esercizio_11();
