import sys
import math
import collections
import numpy as np
from time import perf_counter

# A list to hold benchmarking data which consists of exercise number and
# execution time
bench_data = []

def print_title(title):
    print(f"\n----- {title} -----")

# A decorator to benchmark exercises
def benchmark(bench_data, exercise_name):
    def wrap(f):
        def wrapped_f(*args):
            print_title(exercise_name)
            t1 = perf_counter()
            f(*args)
            tdelta = round((perf_counter() - t1) * 1000, 3)
            data = {exercise_name: tdelta}
            bench_data.append(data)
            data 
        return wrapped_f
    return wrap

# First algorithm by exploiting dict structure
def count_unique1(tokens):
    #tokens = msg.lower().split(" ")
    result = {}
    for t in tokens:
        try:
            result[t] = result[t] + 1
        except KeyError:
            result[t] = 1
    return result

# Second algorithm using collections.Counter object
def count_unique2(tokens):
    #tokens = msg.lower().split(" ")
    c = collections.Counter(tokens)
    return dict(c)


@benchmark(bench_data, "Exercise #1")
def exercise1():
    # Create a temporary list
    l = []

    # I used 100+1 for upper range to emphasise on upper limit (100) and
    # increase the code readability
    for i in range(1, 100+1):
        # The the first condition is multiplies of both 3 and 5,
        # otherwise it would have passed multiplies of three and five and the
        # output would not have been correct
        if (i % 15) == 0:
            msg = "HelloWorld"
            l.append(msg)
        if (i % 3) == 0:
            msg = "Hello"
            l.append("Python")
        elif (i % 5) == 0:
            msg = "World"
            l.append("Works")
        else:
            msg = f"{i}"
            l.append(msg)

        final_tuple = tuple(l)
        print(msg)

    print(f"The final tuple: ", end="")
    print(final_tuple)

@benchmark(bench_data, "Exercise #2")
def exercise2():
    print_title("Problem #2")
    x = sys.argv[1]
    y = sys.argv[2]
    print(f"Original values: x = {x}, y = {y}")

    y, x = x, y
    print(f"After swapping:  x = {x}, y = {y}")


@benchmark(bench_data, "Exercise #3")
def exercise3():
    # Create a lambda function because the calculation can be made in a single line
    calc_distance = lambda p1, p2: math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])** 2)

    # Two arbitary points in linear space
    u = (3.0, 0.0)
    v = (0.0, 4.0)
    distance = calc_distance(u, v)
    assert round(distance, 2) == 5.0, "Euclidean distance is wrong"
    print(distance)

    # Two other points
    u = (10.0, 12.0)
    v = (20.0, 30.0)
    distance = calc_distance(u, v)
    assert round(distance, 2) == 20.59, "Euclidean  distance is wrong"
    print(distance)


@benchmark(bench_data, "Exercise #4")
def exercise4():
    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"

    d1 = count_unique1(s1.lower())
    d2 = count_unique2(s1.lower())
    print(d1)

    # Check both algotithms behaving the same way
    assert d1 == d2

    d1 = count_unique1(s2.lower())
    d2 = count_unique2(s2.lower())
    print(d1)

    # Check both algotithms behaving the same way
    assert d1 == d2


@benchmark(bench_data, "Exercise #5")
def exercise5():
    # Sample input
    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

    # I used the same function from previous problem, because those functions
    # don't care about input type, whether string or list, since both can be tokenized
    unique_nums = count_unique1(l)
    print(unique_nums)

@benchmark(bench_data, "Exercise #6")
def exercise6():
    var1 = sys.argv[1]
    var2 = sys.argv[2]

    try:
        var1 = float(var1)
        var2 = float(var2)
        addition = var1 + var2
        print(addition)
    except ValueError:
        print("Worong input(s). Summation can't be performed")



@benchmark(bench_data, "Exercise #7")
def exercise7():
    l1 = []
    for x in range(10+1):
        l1.append(x**3)
    print(f"Using for loop:\n{l1}")

    l2 = [x**3 for x in range(0, 10+1)]
    print(f"Using list comperhension:\n{l2}")



@benchmark(bench_data, "Exercise #8")
def exercise8():
    a = [(x, y) for x in range(3) for y in range(4)]
    print(a)


@benchmark(bench_data, "Exercise #9")
def exercise9():
    l = [(a, b, c)
         for c in range(100) \
         for a in range(c) \
         for b in range(c) \
         if a**2 + b**2 == c**2]
    t = tuple(l)
    print(t)


@benchmark(bench_data, "Exercise #10")
def exercise10():
    # An example vector
    vector = np.array([1, 2, 3, 4, 5, 6, 7, 9, 9])

    # Normalized vector
    norm_vector = vector / np.sqrt(np.sum(vector**2))

    # Print them out
    print(f"Original vector:\n{vector}")
    print(f"Normalized vector:\n{norm_vector}")

    # Check the squared summ of normalized vector, must be 1.0
    ss = np.sum(norm_vector**2)
    print(f"Squared sum: {ss}")


@benchmark(bench_data, "Exercise #11")
def exercise11():
    l = [0, 1]
    while len(l) < 20:
        l.append(l[-1] + l[-2])
    print(l)

# Execute exercises
exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
exercise8()
exercise9()
exercise10()
exercise11()

# Print benchmarking data
print_title("Benchmark data")
for d in bench_data:
    name, t = list(d.items())[0]
    print(f"{name}: {t} ms")


