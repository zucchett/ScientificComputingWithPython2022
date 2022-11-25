import numpy as np
import bench
import math
import timeit


@bench.benchmark("Exercise #1")
def exercise1():
    m = np.arange(12).reshape((3, 4))
    total_mean = m.mean()
    rows_mean = m.mean(axis=0)
    cols_mean = m.mean(axis=1)

    print(f"Total mean: {total_mean}")
    print(f"Rows mean:  {rows_mean}")
    print(f"Cols mean:  {cols_mean}")


@bench.benchmark("Exercise #2")
def exercise2():
    u = np.array([1, 3, 5, 7])
    v = np.array([2, 4, 6, 8])

    # Method #1
    print("Numpy's outer:")
    o1 = np.outer(u, v)
    print(o1)

    print("List comperhension:")
    o2 = [[i * j for j in v] for i in u]
    print(o2)

    # TODO: broadcasting


@bench.benchmark("Exercise #3")
def exercise3():
    a = np.random.uniform(low=0, high=3, size=(10, 6))
    print(a)
    # TODO
    a[a < 0.3] = 0
    print(a)


@bench.benchmark("Exercise #4")
def exercise4():
    a1 = np.linspace(0, 2 * math.pi, 100, endpoint=True)
    print(a1)
    print(a1[::10])
    print(a1[::-1])

    # TODO: Check the result
    f1 = lambda x: np.abs(np.sin(x) - np.cos(x)) < 0.1
    print(a1[f1(a1)])

    # TODO: plot


@bench.benchmark("Exercise #5")
def exercise5():
    a1 = np.array(list(range(1, 10 + 1)))
    mul_table = np.outer(a1, a1)

    trace = np.trace(mul_table)
    print(f"Matrix trace: {trace}")

    anti_diag = np.diag(mul_table[:, -1::-1])
    print(f"Anti-diag: {anti_diag}")

    off_diag = np.diag(mul_table[:, 1:])
    print(f"1-offset diag: {off_diag}")


@bench.benchmark("Exercise #6")
def exercise6():
    dists = np.array([[0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448]])
    tbl = np.abs(dists - dists.T)
    print(tbl)


@bench.benchmark("Exercise #7")
def exercise7():
    def compute_primes(n):
        mask = np.full((n + 1), True)
        for i in range(2, int(np.sqrt(n)) + 1):
            if not mask[i]:
                continue
            for j in range(i**2, n + 1, i):
                mask[j] = False

        return np.array(range(n + 1))[mask]

    prime_99 = compute_primes(99)
    print(prime_99)

    t99 = timeit.timeit(lambda: compute_primes(99), number=1)
    t999 = timeit.timeit(lambda: compute_primes(999), number=1)
    print(t99)
    print(t999)


@bench.benchmark("Exercise #8")
def exercise8():
    NWALKER = 10
    NSTEP = 20
    tbl = np.random.choice([1, -1], (NWALKER, NSTEP))
    print(tbl)
    dists = tbl.sum(axis=0)
    dists_sq = dists**2
    print(dists)
    print(dists_sq)

    mean = dists_sq.mean()
    print(mean)


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise7()
exercise8()
