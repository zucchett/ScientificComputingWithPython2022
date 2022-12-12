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

    print("Broadcasting operations:")
    uu = np.tile(u, (v.size,1)).T
    o3 = uu * v
    print(o3)


@bench.benchmark("Exercise #3")
def exercise3():
    a = np.random.uniform(low=0, high=3, size=(10, 6))
    print(a)
    a[a < 0.3] = 0
    print(a)

import matplotlib.pyplot as plt

@bench.benchmark("Exercise #4")
def exercise4():
    a1 = np.linspace(0, 2 * math.pi, 100, endpoint=True)
    print("100 values from 0 to 2*pi:")
    print(a1)
    print("\n")

    print("Every 10th element:")
    print(a1[9::10])
    print("\n")

    print("Reverse original array:")
    print(a1[::-1])
    print("\n")

    # Find places where sin and cos get close to each other
    diffs = np.abs(np.sin(a1) - np.cos(a1))
    annot_x = a1[np.where(diffs < 0.1)]
    annot_y = np.sin(annot_x)

    # Plot sin anc cos functions
    plt.plot(a1, np.sin(a1), color='r', label="sin")
    plt.plot(a1, np.cos(a1), color='g', label="cos")

    # Annotate near points
    for loc in zip(annot_x, annot_y):
        plt.annotate('Close sin/cos values', xy=(loc[0], loc[1]),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.005),
            horizontalalignment='right', verticalalignment='top',
        )

    plt.legend()
    plt.show()


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
