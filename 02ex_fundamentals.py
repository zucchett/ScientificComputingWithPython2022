from time import perf_counter
import timeit
import bench

bench_data = bench.BenchData()


@bench.benchmark("Exercise #1", bench_data)
def exercise1():
    def f(alist, x):
        new_list = alist.copy()
        for i in range(x):
            new_list.append(i)
        return new_list

    alist = [1, 2, 3]
    ans = f(alist, 5)
    print(ans)
    print(alist)


@bench.benchmark("Exercise #2", bench_data)
def exercise2():
    orig_ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
    my_ans = [x * x for x in range(10) if x % 2 == 1]

    print(f"Original ans: {orig_ans}")
    print(f"My ans:       {my_ans}")
    assert my_ans == orig_ans, "Problem in exercise2"


@bench.benchmark("Exercise #3", bench_data)
def exercise3():
    def filter_words(word_list, n):
        less_than_n = lambda letter: len(letter) < n
        return list(filter(less_than_n, word_list))

    sample1 = "This is a sample list of words".split(" ")
    print(filter_words(sample1, 2))
    print(filter_words(sample1, 4))
    print(filter_words(sample1, 6))


@bench.benchmark("Exercise #4", bench_data)
def exercise4():
    lang = {"Python": 3, "Java": "", "Cplusplus": "test", "Php": 0.7}
    keys_len = list(map(lambda x: len(x), lang.keys()))
    print(keys_len)


@bench.benchmark("Exercise #5", bench_data)
def exercise5():
    language_scores = [("Python", 97), ("Cplusplus", 81), ("Php", 45), ("Java", 32)]
    l = lambda x: x[0]
    language_scores.sort(key=l)
    print(language_scores)


@bench.benchmark("Exercise #6", bench_data)
def exercise6():
    f1 = lambda x: x**2
    f2 = lambda x: x**3
    mynum = 2

    result = f1(2) * f2(2) * mynum
    print(result)

    assert result == (mynum**6)


def hello(f):
    def wrap(*args):
        print("Hello World!")
        return f(*args)

    return wrap


@hello
def square(x):
    return x * x


@bench.benchmark("Exercise #7", bench_data)
def exercise7():
    print("Before calling square()")
    print(square(10))
    print("After calling square()")


@bench.benchmark("Exercise #8", bench_data)
def exercise8():
    # Fist recursive implementation
    def fibonacci_recursive_1(n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            return fibonacci_recursive_1(n - 1) + fibonacci_recursive_1(n - 2)

    # Second recursive implementation using a cache
    # Use a dictionary object to store already computed numbers
    fibonacci_cache = {}

    def fibonacci_recursive_2(n):
        if n == 0:
            ret = 0
        elif n <= 2:
            ret = 1
        elif n in fibonacci_cache:
            return fibonacci_cache[n]
        else:
            ret = fibonacci_recursive_1(n - 1) + fibonacci_recursive_1(n - 2)

        # Add computed number to cache
        fibonacci_cache[n] = ret
        return ret

    # Compute the first 20 fibinacci numbers by the first algorthm
    def test1():
        fib20 = []
        for i in range(20):
            fib20.append(fibonacci_recursive_1(i))
        return fib20

    # Compute the first 20 fibinacci numbers by the second algorthm
    def test2():
        fib20 = []
        for i in range(20):
            fib20.append(fibonacci_recursive_2(i))
        return fib20

    # Comparing these two implementations:
    # Obviousely using cache memory improves the performence significantly.
    # Witout cache, The same sequence number over must be computed over and
    # over again. By using cache memory, after the first run, it simply
    # retrives the computed number from the cache, hence the execution
    # time mostly depends on access time of the data structure used in the
    # cache memory (Dictionary in this case)
    t1 = timeit.timeit(lambda: test1(), number=500)
    t2 = timeit.timeit(lambda: test2(), number=500)
    print(f"Execution time of recursive algorithm WITHOUT cache: {t1*1000} ms")
    print(f"Execution time of recursive algorithm WITH cache:    {t2* 1000} ms")


@bench.benchmark("Exercise #9", bench_data)
def exercise9():
    msg = """
    Compare to the implementation in the first exercise (using while loop):
    Both of these recursive implementations, have weaker performance.
    Because, calling a function (jump to the function and return, preparing
    the stack, etc) is more expensive than cycling in a loop
    """
    print(msg)


class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("At lease 3 sides are needed for a polygon")
        self._sides = list(sides)

    @property
    def sides(self):
        return tuple(self._sides)

    def get_side(self, index):
        return self._sides[index]

    def set_side(self, index, new_value):
        self._sides[index] = new_value

    def perimeter(self):
        return sum(self._sides)

    def getOrderedSides(self, increasing=True):
        # Make a copy of original sides and then sort it. I preserved the
        # original shape of sides variable in order to not messed up with
        # `set_side` and `get_side` methods, since the user expects the original
        # shape (index) for side variable as the object has constructed with it.
        sorted = self._sides.copy()
        sorted.sort(reverse=not increasing)
        return sorted


class Rectangle(Polygon):
    # Override the original constructor
    def __init__(self, length, width):
        # Create the sides in clockwise orientation
        # The index of each element in `_sides` variable is
        # shown in figure below:
        #
        #      _____Length_(0)__
        #     |                 |
        # (3) |                 | Width (1)
        #     |_________________|
        #             (2)

        self._sides = [length, width, length, width]

    # Introduce a new method
    def area(self):
        return self._sides[0] * self._sides[1]


@bench.benchmark("Exercise #10", bench_data)
def exercise10():
    sides = (10, 20, 15, 5)
    poly1 = Polygon(sides)

    # Show current sides
    print(f"Current sides of poly: {poly1.sides}")

    p = poly1.perimeter()
    print(f"Perimeter of poly: {p}")
    assert p == sum(sides)

    s1 = poly1.getOrderedSides()
    s2 = poly1.getOrderedSides(increasing=False)
    print(f"Increasing order of sides: {s1}")
    print(f"Decreasing order of sides: {s2}")
    assert s1 == sorted(sides)
    assert s2 == sorted(sides, reverse=True)

    # Change the first element of sides
    poly1.set_side(0, 100)
    assert poly1.sides == (100, 20, 15, 5)

    # Try to change a missing side
    try:
        poly1.set_side(4, 123)
    except IndexError as e:
        print(str(e))

    # Try to construct a polygon with less than three sides
    try:
        poly2 = Polygon((1, 2))
    except ValueError as e:
        print(str(e))


@bench.benchmark("Exercise #11", bench_data)
def exercise11():
    length, width = 10, 5
    rect = Rectangle(length, width)
    area = rect.area()
    print(f"Rectangle sides: {rect.sides}")
    print(f"Rectangle area:  {area}")

    # Perform some tests
    assert rect.sides == (length, width, length, width)
    assert rect.area() == length * width


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

print("\n----- Runtime statistics -----")
print(bench_data)
