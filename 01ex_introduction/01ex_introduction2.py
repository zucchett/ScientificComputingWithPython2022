x = str(input("Enter First variable x: "))
y = str(input("Enter Second variable y: "))
x = x + "/n" + y
y = x.split("/n")[0]
x = x.split("/n")[1]

print("First Value that you entered is: "+ x)
print("Second Value that you entered is: "+ y)
# print(type(x))
