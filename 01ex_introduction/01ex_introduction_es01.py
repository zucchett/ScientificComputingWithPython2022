helloworld_list = []
for i in range(1, 101):
    if i% 15 == 0:
        x = "Hello world"
    elif i % 3 == 0:
        x = "Hello"
    elif i% 5 == 0:
        x = "world"
    else:
        x = i
    print(x)
    helloworld_list.append(x)
print(helloworld_list)
for i, v in enumerate(helloworld_list):
    if v == "Hello":
        helloworld_list[i] = "Python"
    if v == "world":
        helloworld_list[i] = "Works"
helloworld_tuple = tuple(helloworld_list)
print('----------------------------------------------------')
print(helloworld_tuple)

