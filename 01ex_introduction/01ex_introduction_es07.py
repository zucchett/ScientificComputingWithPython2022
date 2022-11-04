# 7\. **Cubes**
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# a) a for loop
# b) a list comprehension
# 7\. **立方体**
# 为*[0, 10]*中的*x*创建一个三次方的列表。
# a) 一个for循环
# b) 列表理解


# a) a for loop
cubes = []
for i in range(0, 11):
    cubes.append(i**3)
print("cubes", cubes)

# b) a list comprehension
cubes2 = [i**3 for i in range(0, 11)]
print("cubes2", cubes2)




