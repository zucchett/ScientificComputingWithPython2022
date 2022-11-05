def recursiveFibonacci(n):  
    if n <= 1:  
        return n  
    else:  
        return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))
    
length = 20  
for i in range(length):
    print(recursiveFibonacci(i)) 