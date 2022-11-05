#6. Casting

print("Insert two integers, floats or strings: ")
var1 = input()
var2 = input()


try:
    print(float(var1)+float(var2))
except:
    print(var1+var2)