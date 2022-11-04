# 8. The Fibonacci sequence (part 2)
# Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
lista=[0,1]
def fibonacci(n,i):
  global lista
  if i <n:
    lista.append(lista[i-2]+lista[i-1])
    fibonacci(n,i+1)
  else:
    print(lista)
fibonacci(20,2)
print(len(lista))


