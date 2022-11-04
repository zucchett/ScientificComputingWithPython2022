def recursive_f(n):
    fibonacci = []
    def find_f(n):
        if (n <= 2):
            a = n-1
        else:
            a = find_f(n-2)+find_f(n-1)
        if (len(fibonacci) == n-1):
            fibonacci.append(a)
        return a
    find_f(n)
    return fibonacci

print(recursive_f(20))