import math
import numpy as np
from bench import benchmark
import timeit
import time
from bench import benchmark


@benchmark("Exercise1")
def exercise1():
    def change_base(in_string: str, base=10) -> str:
        # The first two character in input string can be 0x for hex and
        # 0b for binary, otherwise it will assume as decimal number
        in_string = in_string.strip().lower()
        prefix = in_string[:2]
        if prefix == "0b":
            num = int(in_string[2:], 2)
        elif prefix == "0x":
            num = int(in_string[2:], 16)
        else:
            num = int(in_string)

        if base == 2:
            return bin(num)
        elif base == 16:
            return hex(num)
        elif base == 10:
            return str(num)

    # Normal behaviour
    assert change_base("0x11", 2) == "0b10001"
    assert change_base("12", 2) == "0b1100"
    assert change_base("0b10011", 10) == "19"

    # It throws an exception in case of bad inputs
    try:
        change_base("abcd")
    except ValueError as e:
        print(e)

    try:
        change_base("0b123")
    except ValueError as e:
        print(e)


@benchmark("Exercise2")
def exercise2():
    def bin_to_float(bin_str: str) -> float:
        # Remove possible leading and trailing spaces
        bin_str.strip()
        # Lenght must be exactly 32 chars
        if len(bin_str) != 32:
            raise ValueError("Bad input binary string")

        s = int(bin_str[0], 2)
        e = int(bin_str[1:9], 2)
        f = int(bin_str[9:], 2)

        # Special values
        if e == 255 and f == 0:
            return float("+inf") if s == 0 else float("-inf")
        elif e == 255 and f > 0:
            return float("nan")

        mantissa = 1.0
        for i, m in enumerate(bin_str[9:], 1):
            mantissa += int(m) / 2**i

        return (-1) ** s * mantissa * 2 ** (e - 127)

    # 1.316554e-36
    print(bin_to_float("00000011111000000000000000000000"))
    # -5.500000
    print(bin_to_float("11000000101100000000000000000000"))
    # +inf
    print(bin_to_float("01111111100000000000000000000000"))
    # -inf
    print(bin_to_float("11111111100000000000000000000000"))
    # NaN
    print(bin_to_float("01111111100000000000000000000001"))


@benchmark("Exercise3")
def exercise3():
    # Init a variable
    i = 1.0
    # Use for loop rather than while, to avoid getting stuck in an infinite loop
    for _ in range(2000):
        # Keep doubling until it hits the infinity
        j = i * 2
        if j == float("+inf"):
            break
        i = j
    print(f"Overflow limit (factor of 2): {i}")

    i = 1.0
    for _ in range(2000):
        j = i / 2
        if j == 0.0:
            break
        i = j
    print(f"Underflow limit (factor of 2): {i}")


@benchmark("Exercise4")
def exercise4():
    last_hex = ""
    for e in range(0, -32, -1):
        h = (1.0 + 10**e).hex()
        if h == last_hex:
            break
        last_hex = h
    print(f"Machine precision: {10**e}")


@benchmark("Exercise5")
def exercise5():
    def quad1(a, b, c):
        print("Standard Formula:")
        x1 = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
        return x1, x2

    def quad2(a, b, c):
        # Multipling numerator and denominator by a factor will scale up the
        # numbers, hence they can be represent more accurately by floating
        # point variables which leads to more accurate results
        print("Multiplying by numerator:")
        i = b**2 - (4 * a * c)
        i = math.sqrt(i)
        n = -b + i
        x1 = (n * n) / (2 * a * n)

        n = -b - i
        x2 = (n * n) / (2 * a * n)
        return x1, x2

    def quad3(a, b, c):
        # Using float128 give us more accuracy in computations
        print("Float128:")
        a = np.float128(a)
        b = np.float128(b)
        c = np.float128(c)
        x1 = (-b + np.sqrt(np.power(b, 2) - (4 * a * c))) / (2 * a)
        x2 = (-b - np.sqrt(np.power(b, 2) - (4 * a * c))) / (2 * a)
        return x1, x2
        print(x1)

    def quad4(a, b, c):
        # On the other hand, with float32 we have less accurate results
        print("Float32:")
        a = np.float32(a)
        b = np.float32(b)
        c = np.float32(c)
        x1 = (-b + np.sqrt(np.power(b, 2) - (4 * a * c))) / (2 * a)
        x2 = (-b - np.sqrt(np.power(b, 2) - (4 * a * c))) / (2 * a)
        return x1, x2
        print(x1)

    a = 0.001
    b = 1000
    c = 0.001
    print(f"Calculatig: {a}x^2 + {b}x + {c} = 0")
    for f in [quad1, quad2, quad3, quad4]:
        x1, x2 = f(a, b, c)
        print(f"x1={x1}, x2={x2}\n")


@benchmark("Exercise6")
def exercise6():
    def derivative(f, x, delta=1e-2):
        return (f(x + delta) - f(x)) / delta

    # Define an arbitrary function to compte its derivative
    f1 = lambda x: x * (x - 1)

    # The best accuracy accross different delta values is when
    # the delta is small enough. But, extremely small values can't
    # be stored in floating point variables and lead to computational
    # errors. In the list of delta values down here, the best accuracy
    # is achieved with delta equal to: 1e-8

    for delta in [1e-2, 1e-4, 1e-6, 1e-8, 1e-12, 1e-14]:
        d = derivative(f1, x=1, delta=delta)
        # Difference between the result and ground truth
        offset = np.float128(1.0) - d
        print(f"delta: {delta}, derivative: {d}, offset: {offset}")


@benchmark("Exercise7")
def exercise7():
    f = lambda x: math.sqrt(1 - x**2)

    def riemann(func, start, stop, N):
        h = np.abs(start - stop) / N
        s = 0
        for x in np.linspace(start, stop, N):
            s += f(x) * h
        return s

    i = riemann(f, -1.0, 1.0, 100)
    print(f"Riemann result with N=100: {i}")
    offset = (math.pi / 2) - i
    print(f"Offset with real value: {offset}")

    print("Runtimes for computing Riemann with various N values:")
    N = 100
    # Keep doubling N up to 50 times (just a deterministic guess) in order
    # to find a value for N that increases runtime beyond one second.
    for i in range(50):
        n = N * 2
        t1 = timeit.timeit(lambda: riemann(f, -1.0, 1.0, n), number=1)
        print(f"\tN={n}: {round(t1, 3)} sec")
        if t1 > 1.0:
            break
        N = n
    print(f"Optimum N value to keep the runtime less than a second: {N}")

    # A heuristic way to compute N value which increases runtime to
    # 60 second. It uses the last N value from previous section and
    # compute the ratio, then multiply the last N value by this ratio.
    # Runtime would not be exact 60 seconds, but somewhere around it.
    n_60sec = int((60 / t1) * n)
    t1 = time.perf_counter()
    result = riemann(f, -1.0, 1.0, n_60sec)
    runtime = time.perf_counter() - t1
    print(f"N: {n_60sec}, Result: {result}, Runtime: {runtime}")


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
