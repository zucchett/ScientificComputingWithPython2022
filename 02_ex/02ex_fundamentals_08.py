def fibonacci_sequence(i, fibonacci_list=None):

    if fibonacci_list is None:
        fibonacci_list = []
    if i == 0:
        return fibonacci_list
    if len(fibonacci_list) == 0:
        fibonacci_list.append(0)
    elif len(fibonacci_list) == 1:
        fibonacci_list.append(1)
    else:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    fibonacci_sequence(i - 1, fibonacci_list)
    return fibonacci_list
print("The first 20 Fibonacci numbers: ", fibonacci_sequence(20))