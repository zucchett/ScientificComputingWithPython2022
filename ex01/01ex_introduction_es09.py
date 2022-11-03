def pythagorean(i):
    c, m = 0, 2
    while c < i:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > i:
                break

            print(a, b, c)

        m = m + 1

i = 100
pythagorean(i)