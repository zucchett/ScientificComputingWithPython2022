import timeit
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    m = 2
    while (m * m <= n):

        if (prime[m] == True):

            for i in range(m ** 2, n + 1, m):
                prime[i] = False
        m += 1
    prime[0]= False
    prime[1]= False

    for m in range(n + 1):
        if prime[m]:
            print (m)
start_time = timeit.default_timer()
SieveOfEratosthenes(1000)
print("The time difference is :", timeit.default_timer() - start_time)