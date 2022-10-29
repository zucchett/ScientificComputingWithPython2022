def fibonacci_sequence(i, fibo_list=None):
    if fibo_list is None:
        fibo_list = []
    if i == 0:
        return fibo_list
    if len(fibo_list) == 0:
        fibo_list.append(0)
    elif len(fibo_list) == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    fibonacci_sequence(i - 1, fibo_list)
    return fibo_list


print("The first 20 numbers of the Fibonacci sequence are: ", fibonacci_sequence(20))
