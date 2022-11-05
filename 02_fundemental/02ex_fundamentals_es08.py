def fibonacci_seq(n):
    fibonacci_list = []
    
    for n in range(n):
        if n <= 1 :
            fibonacci_list.append(n)
        else:
            fibonacci_list.append(fibonacci_list[n-1] + fibonacci_list[n-2])
    return fibonacci_list

fibonacci_seq(20)

def fibonacci_seq(n):
    
    if n <= 1 :
        return n
    else:
        v = fibonacci_seq(n-1) + fibonacci_seq(n-2)
        return v

n = 20

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci_seq(i))
    
    