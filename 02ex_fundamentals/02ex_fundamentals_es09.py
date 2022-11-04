import timeit

loopFibonacci = '''
i, first, second, length = 0, 0, 1, 20
           
while(i < length):
    if(i <= 1):
        count = i
    else:
        count = first + second
        first = second
        second = count
    print(count)
    i += 1
'''

recursiveFibonacci = '''
def recursiveFibonacci(n):  
    if n <= 1:  
        return n  
    else:  
        return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))
    
length = 20  
for i in range(length):
    print(recursiveFibonacci(i)) 
'''

print("loopFibonacci: ")
%timeit loopFibonacci
print("recursiveFibonacci: ")
%timeit recursiveFibonacci