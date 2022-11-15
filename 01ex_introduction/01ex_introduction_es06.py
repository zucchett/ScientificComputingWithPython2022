# 6\. **Casting**
#
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.
# * 从命令行中读取两个变量，这两个变量可以是`int`，`float`，或者`str`。
# * 使用`try`/`except`表达式来执行这两个变量的相加，如果可能的话
# * 打印结果而不使代码在所有`int`/`float`/`str`的输入组合中崩溃。

def countNum(a, b):
    try:
        x = a + b
        print(x)
    except:
        print(a, b)
    return

countNum(3, "yyy")
