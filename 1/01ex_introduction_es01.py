# The HelloWorld replacement

results = []
for i in range (1,101):
    print(i)
    res = ""
    if i % 3 == 0 and i % 5 == 0:
        res = "HelloWorld"
        results.append((i,res))
    elif i % 3 == 0:
        res = "Hello"
        results.append((i,res))
    elif i % 5 == 0:
        res = "World"
        results.append((i,res))
    print(res)

counter = 0
for i in results:
    if "Hello" in i[1]:
        list_i = list(i)      
        list_i[1] = list_i[1].replace('Hello', 'Python')
        i = tuple(list_i)
        results[counter] = i

    if "World" in i[1]:
        list_i = list(i)       
        list_i[1] = list_i[1].replace('World', 'Works')
        i = tuple(list_i)
        results[counter] = i

    counter = counter + 1

print(results)