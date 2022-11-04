def loopFibunacci(n):
     
     # n=int(input("enter number : "))
     n1, n2 = 0, 1 # first two terms of fibonacci series
     i = 0  #variable for loop
 
     print("Fibonacci sequence for 10 :")
     for i in range(n):  
        print(n1)
        sum = n1 + n2  
        n1 = n2
        n2 = sum
        i += 1
loopFibunacci(10)