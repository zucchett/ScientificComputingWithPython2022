
import timeit
input('enter anything to continue to speed test')
print('Question 9')
start_time = timeit.default_timer()
print('start time: ', start_time)
loopFibonacci(20)
print("difference: ", timeit.default_timer() - start_time)
start_time = timeit.default_timer()
print('start time: ', start_time)
for i in range(20):
    print(recursiveFibonacci(i))
print("difference: ", timeit.default_timer() - start_time)