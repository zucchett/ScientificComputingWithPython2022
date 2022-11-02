# 8. The Fibonacci sequence (part 2)

# Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.

# -------------------------------------- Code Begin-------------------------------------

def fibonacci(n):
    if n == 0 :
        return 0
    elif n==1 or n==2:
        return 1
    else :
        return fibonacci(n-1) +  fibonacci(n-2)


for i in range(20):
    print('F({}) = {}'.format(i,fibonacci(i)))

# -------------------------------------- Code End ---------------------------------------

    
