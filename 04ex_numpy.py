import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import math
import timeit

def esercizio1():
    #Find the row, column and overall means for the following matrix:
    m = np.arange(12).reshape((3,4))
    print(m)

    print(np.mean(m)) #Overall mean
    print(np.mean(m,axis=0)) #Mean for every column
    print(np.mean(m,axis=1)) #Mean for every row

def esercizio2():
    #Find the outer product of the following vectors:
    u = np.array([1, 3, 5, 7])
    v = np.array([2, 4, 6, 8])

    #1. Using the function `outer` in numpy
    #2. Using a nested `for` loop or a list comprehension
    #3. Using numpy broadcasting operations

    #1
    Op1=np.outer(u,v)
    print(Op1)
    #2
    Op2= np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            Op2[i][j]=u[i]*v[j]
    print(Op2)
    #3
    Op3=u[:, None]*v
    print(Op3)

def esercizio3():
    #Create a 10 by 6 matrix of float random numbers, distributed between 0 and 3 according to a flat distribution.
    #After creating the matrix, set all entries< 0.3 to zero using a mask.
    Values=3*npr.rand(10, 6)
    print(Values)
    Values[Values < 0.3] = 0
    print(Values)

def esercizio4():
    #Use `np.linspace` to create an array of 100 numbers between 0 and 2pi (inclusive).

    #Extract every 10th element using the slice notation
    #Reverse the array using the slice notation
    #Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
    #Optional: make a plot showing the sin and cos functions and indicate where they are close

    vec=np.linspace(0,np.pi,100)
    print(vec)

    print(vec[::10])
    print(vec[::-1])

    extraction=[]
    for value in vec:
        if abs(np.sin(value)-np.cos(value))<0.1:
            extraction.append(value)

    print(extraction)
    plt.plot(vec,np.sin(vec))
    plt.plot(vec,np.cos(vec))
    plt.axis([0.7,0.9,0.6,0.8])
    plt.show()

def esercizio5():
    #Create a matrix that shows the 10 by 10 multiplication table.

    #Find the trace of the matrix
    #Extract the anti-diagonal matrix (this should be ```array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10])```)
    #Extract the diagonal offset by 1 upwards (this should be ```array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])```)
    mul= np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            mul[i][j]=(i+1)*(j+1)

    print(mul)
    print(np.trace(mul))

    mul_arr=np.matrix.flatten(mul)
    print(mul_arr)
    for i in range(10):
        print(mul_arr[9+i*9])
    print("Diagonal offset by 1")

    for j in range(9):
        print(mul_arr[1+j*11])

def esercizio6():
    #Use broadcasting to create a grid of distances.
    #Route 66 crosses the following cities in the US: 
    #Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.
    #The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448
    #Build a 2D grid of distances among each city along Route 66
    #Convert the distances in km
    distances=[0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448]
    distances_grid= np.zeros((len(distances), len(distances)))
    for i in range(len(distances)):
        for j in range(len(distances)):
            distances_grid[i][j]=abs(distances[j]-distances[i])
    print(distances_grid)
    distances_grid=np.multiply(distances_grid, 1.60934)
    print(distances_grid)

def esercizio7():
    #Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
    #Constract a shape (N,) boolean array, which is the mask
    #Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
    #Apply the mask to obtain an array of ordered prime numbers
    #Check the performances (with `timeit`); how does it scale with N?
    #Implement the optimization suggested in the sieve of Eratosthenes

    N=100
    def basic_method(N=100):
        numbers=np.linspace(1,N,N)
        mask=[True]*N #Set False if i-th value is not prime
        mask[0]=False

        for i in range(2,N):
            for j in range(2,N):
                if numbers[i]%numbers[j]==0 and numbers[i]!=numbers[j]:
                    mask[i]=False
                    break
        primes=[]
        for i in range(N):
            if mask[i]:
                primes.append(i+1)

    def eratostene(N=100):
        numbers=np.linspace(1,N,N)
        p=2
        numbers[0]=0
        primi=[]
        
        while p<=int(math.sqrt(N)):
            for i in range (1,N):
                numbers[i]=int(numbers[i])
                if (numbers[i]!=p and numbers[i]%p==0):
                    numbers[i]=0
            p=p+1
        for j in range(0,N):
            if (numbers[j] != 0):
                primi.append(int(numbers[j]))

    basic_method(N)
    eratostene(N)
    print(timeit.timeit(basic_method,number=100))# We get 0.129988231
    print(timeit.timeit(eratostene,number=100))# We get 0.11135346200000007
    
    n=[100, 150,300,400,600,750,1000,1500,2000,3500,5000]
    tempo=[]
    for elements in n:
        starttime = timeit.default_timer()
        eratostene(elements)
        tempo.append(timeit.default_timer() - starttime)
        
    plt.plot(n,tempo)
    plt.show()
    #L'andamento del grafico sembra essere leggermente esponenziale.


def esercizio8():
    #Consider a simple random walk process: at each step in time, a walker jumps right or left (+1 or -1) with equal probability. 
    #The goal is to find the typical distance from the origin of many random walkers after a given amount of time.
    #Hint: create a 2D array where each row represents a walker, and each column represents a time step.

    #Take 1000 walkers and let them walk for 200 steps
    #Use `randint` to create a 2D array of size $walkers \times steps$ with values -1 or 1
    #Calculate the walking distances for each walker (e.g. by summing the elements in each row)
    #Take the square of the previously-obtained array (element-wise)
    #Compute the mean of the squared distances at each step (i.e. the mean along the columns)
    #Optional: plot the average distances (sqrt(distance^2)) as a function of time (step)
    walkers=1000
    steps=20

    Matrix=npr.randint(0, 2, size=(walkers, steps))
    Matrix[Matrix==0] = -1
    #print(Matrix)

    #Parte relativa alle righe
    sum_Rows=np.sum(Matrix, axis=1)
    #print(sum_Rows)
    Mean=np.mean(np.sqrt(np.square(sum_Rows)))
    print(Mean)

    #Parte relativa alle colonne:
    sum_Columns=np.sum(Matrix, axis=0)
    print(sum_Columns)
    Mean_c=np.sqrt(np.square(sum_Columns))/walkers #Distanza media percorsa per ogni step
    print(Mean_c)#Incremento medio per ogni colonna
    #Viene calcolata la distanza media dello step+la distanza precedente
    Mean_c_previous=np.zeros(len(Mean_c))
    for i in range(len(Mean_c)):
        for j in range(i+1):
            Mean_c_previous[i]=Mean_c_previous[i]+Mean_c[j]
    print(Mean_c_previous)#Incremento medio totale ad ogni step(colonna attuale+ media delle precedenti)

