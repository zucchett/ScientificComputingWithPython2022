# The HelloWorld replacement
#A
results =[]
for i in range(1,101):
   if i % 5 == 0 and i % 3 == 0:
      i = 'HelloWorld'
      print(i)
      results.append(i);
   elif i % 3 == 0:
      i = 'Hello'
      print(i)
      results.append(i)
   elif i % 5 == 0:
      i = 'World'
      print(i)
      results.append(i)
   else:
      print(i)
      results.append(i)
a = tuple(results)
print(a)

#B

results = list(a)
for i in range(len(results)):
    if results[i] == 'Hello':
        results[i] = 'Python'

    if results[i] == 'World':
        results[i] = 'Works'

b = tuple(results)
print(b)
