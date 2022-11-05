a = input ("Enter first variable : ")
print("a : ", a)
b = input ("Enter seconf variable : ")
print("b : ",b)
a, b = b, a
print("-----------------", "After Swap", sep="\n")
print("a : ", a)
print("b : ",b)