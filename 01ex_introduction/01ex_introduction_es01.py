# 1. The HelloWorld replacement
# a) Write a program that:
# prints the numbers from 1 to 100
# but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
# for numbers which are multiples of both three and five print "HelloWorld".
# b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".


#a
list1 = []
for i in range(0,100):
    i += 1
    if i % 3 == 0 & i % 5 == 0:
        list1.append("HelloWorld")
    elif i % 3 == 0:
        list1.append("Hello")
    elif i % 5 == 0:
        list1.append("World")
    else:
        list1.append(i)

print(list1)
print(type(list1))

#b
for index in range(len(list1)):
    if list1[index] == "Hello":
        list1[index] = "Python"
    elif list1[index] == "World":
        list1[index] = "Works"
    elif list1[index] == "HelloWorld":
        list1[index] = "PythonWorks"
tup = tuple(list1)

print(tup)
print(type(tup))


