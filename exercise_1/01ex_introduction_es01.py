first_list = []
for i in range (1,101) :
    if (i % 5 == 0) and (i % 3 == 0):
        first_list.append("HelloWorld")
    elif i % 5 == 0:
        first_list.append('World')
    elif i % 3 == 0:
        first_list.append("Hello")
    else :
        first_list.append(i)
print(first_list)

input('Please insert any key to continue: ')

for x in range(0,len(first_list)) :
    if first_list[x] == "Hello":
        first_list[x] = "Python"
    elif first_list[x] == "World":
        first_list[x] = "Works"
print(first_list)