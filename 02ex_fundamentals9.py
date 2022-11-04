# 9. The Fibonacci sequence (part 3)
# Run both the Fibonacci recursive function from the previous exercise, 
# and the Fibonacci function from 01ex that use only for and while loops.
# Measure the execution code of the two functions with timeit (link to the doc), for example:
import timeit
#####
def loopFibonacci(n):
  fib_seq = [0,1]
  [fib_seq.insert(i+2,fib_seq[i+1] + fib_seq[i]) for i in range(n-2)]
  print(fib_seq)
  return fib_seq
t = timeit.Timer(lambda: loopFibonacci(20))  
print('\nTime for loop function :',t.timeit(1))

# ##
lista=[0,1]
def recursiveFibonacci(n,i):
  global lista
  if i <n:
    lista.append(lista[i-2]+lista[i-1])
    recursiveFibonacci(n,i+1)
  else:
    print(lista)

# print(timeit.repeat(stmt=recursiveFibonacci(20,2), repeat=5))
t = timeit.Timer(lambda: recursiveFibonacci(20,2))  
print('\nTime for recursive function: ',t.timeit(1))
# print(timeit.timeit(stmt='for i in range(100):print(i)',number=1))
print('\nDifferent way of timing function\n')
print('='*100)
#####################3
starttime = timeit.default_timer()

def loopFibonacci(n):
  fib_seq = [0,1]
  [fib_seq.insert(i+2,fib_seq[i+1] + fib_seq[i]) for i in range(n-2)]
  print(fib_seq)
  return fib_seq

print("The start time for loop function is :",starttime)
loopFibonacci(20)
print("The time difference is :", timeit.default_timer() - starttime)

print('='*100)
starttime = timeit.default_timer()
lista=[0,1]
def recursiveFibonacci(n,i):
  global lista
  if i <n:
    lista.append(lista[i-2]+lista[i-1])
    recursiveFibonacci(n,i+1)
  else:
    print(lista)

print("The start time for recursive function is :",starttime)
recursiveFibonacci(20,2)
print("The time difference is :", timeit.default_timer() - starttime)
