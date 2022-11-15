# 4. Counting letters
# Write a program that calculates the number of times each character occurs in a given string.
# Ignore differences in capitalization. The strings are in the cell below.
# 编写一个程序，计算每个字符在给定字符串中出现的次数。忽略大小写差异。字符串在下面的单元格中。
# ascii_list = [ord(i) for i in x] 有一种想法就是把字符串转换成ascii码，然后统计
# print(ascii_list)
# for i in ascii_list:
# num = ascii_list.count(i)


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

from collections import Counter

def CountWords(str):
    # str1 = str.replace(" ", "")
    low_str = str.lower()
    c = Counter(low_str)
    print(c)
    return


CountWords(s2)
CountWords(s1)
