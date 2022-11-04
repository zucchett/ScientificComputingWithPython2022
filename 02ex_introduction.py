
#EXERCISE 1

print( "------------Global variables-----------------")


def f(alist):
    x = 5
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 

#EXERCISE 2
print( "------------List of comprehension-----------------")




#EXERCISE 3

print( "------------Filter list-----------------")

def longw(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words: ").split()
    length = int(input("Words that correspond to the length: "))
    print("Words longer than {} are {}.".format(length,
          ', '.join(longw(words, length))))

main()

#EXERCISE 4

print( "------------Map dictionary-----------------")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
lista=lang.keys();
print ("Dictionaty converted to a list: ", lista)
print ("Lenght of each word",list(map(len,lista)))


#EXERCISE 5

print( "------------Lambda functions-----------------")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print(language_scores)
language_scores.sort(key=lambda x:x[0])
print( "Order alphabetically: ", language_scores)

#EXERCISE 6

print( "------------Nested functions-----------------")

def cubo(num):
    a=3
    b=num**a
    print("Cube is", b)
    def squared(num):
        j=2
        h=num**j
        print("Square is = ", h)
        def six(num):
            m=j+a
            n=num**m
            print("Num ^ 6 = ", n)
        six(2)
            
    squared(2)
    
cubo(2)


#EXERCISE 7

print( "------------Decorators-----------------")
#EXERCISE 8

print( "------------The fibonacci sequence #2-----------------")

def recurfibo(n):
   if n <= 1:
       return n
   else:
       return(recurfibo(n-1) + recurfibo(n-2))
nt = 20

print("Fibonacci sequence:")
for i in range(nt):
    print(recurfibo(i))

#EXERCISE 9

print( "------------The fibonacci sequence #3----------------")

import timeit
import random

#Fibonacci 1

def fibonacci_1():
    n1=0
    n2 = 1
    count = 0

    print("Fibonacci sequence:")

    for nterms in range (20):
        while count < nterms:
            print(n1)
            nth = n1 + n2
        # update values
            n1 = n2
            n2 = nth
            count += 1
        
        
starting_time = timeit.default_timer()
print("\n Start time fibonacci ex1 :",starting_time)

fibonacci_1()
print("Time difference fibonacci ex1 :", timeit.default_timer() - starting_time)


#Function fibonacci 2
def recurfibo(n):
   if n <= 1:
       return n
   else:
       return(recurfibo(n-1) + recurfibo(n-2))

nt = 20

starting_time = timeit.default_timer()
print("\n Second timer for fibonacci 2 ")
print("\n Start time fibonacci ex2 :",starting_time)

print("Fibonacci sequence ex2:")
for i in range(nt):
    print(recurfibo(i))
    recurfibo(i)
    
print("Time difference fibonacci ex2 :", timeit.default_timer() - starting_time)

print("\n\n The most efficent is the one made of loops for and while for 0.009005029000036300 ")




