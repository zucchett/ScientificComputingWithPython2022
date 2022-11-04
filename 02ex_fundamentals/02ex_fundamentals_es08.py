f = [0,1]
def recurs_fib(f):
    if len(f) > 20:
        return f
    else:
        f.append(f[-1] + f[-2])
#        print(f)
        return recurs_fib(f)

print(recurs_fib(f))


    

