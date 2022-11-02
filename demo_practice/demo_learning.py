


#   exercise1 :05,08,09有问题
#   exercise2 :1,5,7,8,9,10,11



#希望输出到文件当中,a+表示以读写的方式打开文件，如果存在这个文件就在文件后面追加内容，如果没有就新建这个文件
# fp = open('d/text.txt', "a+",)
# print('hello', file=fp)
# fp.close()
"""
二二(比特)8 bit = 1byte(字节）  1024byte = 1KB(千)  1024KB= 1MB(兆) 1024MB= 1GB(吉) 1024GB= 1TB(太)

数据类型转换str(),int(),float()当用+链接时候，数据类型需要相同

print(3 / 4) # 整数之间的除法
print(3.0 / 4.0) # 浮点数之间的除法
print(3 % 4) # 取余 modulus
print(3 // 4) # 地面除法floor division
print(3**4) # 指数运算exponentiation
print(pow(3, 4)) # 幂函数 (和上面指数运算的结果相同）power function

从键盘录入整数 a = int(input("请输入一个数据"))
a = [7, 5, 3, 4, 10]
a.sort() #按数字大小排序
a.pop() # remove last element
a.remove(10) # remove by value
a.remove(a[2]) # same as before



a = {'key1' : "anItem", 2 : ["a,bc"], 3.4 : "C", 'fourthkey' : 7} # dictionary example
for i in a: print(i, a[i])
print("Keys:", a.keys())
print("Values:", a.values())

or i, j in enumerate([4, 5, 2, 7]): print(i, j) # unpack the tuple on-the-fly

a is b #is用于比较对象的标识使用 比较id   还有 （a is not b）
"""

#import keyword
#print(keyword.kwlist)输出保留字
list1 = []
list2 = []
# while i < 100:
#     i += 1
for i in range(0 , 101):
    if i % 3 == 0 and i % 5 == 0:
        list1.append("HelloWorld")
        list2.append("PythonWorks")
    elif i % 3 == 0:
        list1.append("Hello")
        list2.append("Python")
    elif i % 5 == 0:
        list1.append("World")
        list2.append("works")
    else:
        list1.append(i)
        list2.append(i)

tup = tuple(list1) #把list转换成tuple
print(list1)

print(list2)
