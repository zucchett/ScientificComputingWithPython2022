"""
1. Text files
Perform the following operations on plain txt files:
create a list of integrer numbers and then save it to a text file named data_int.txt. Run the cat command to print the content of the file.
create a matrix of 5x5 floats and then save it to a text file named data_float.txt. Use the cat command to print the content of the file.
load the txt file of the previous point and convert it to a csv file by hand.
1. 文本文件
对普通txt文件进行以下操作。
创建一个整数列表，然后将其保存在一个名为data_int.txt的文本文件中。运行cat命令来打印文件的内容。
创建一个5x5浮点数的矩阵，然后将其保存到一个名为data_float.txt的文本文件中。使用cat命令打印该文件的内容。
加载上一点的txt文件，用手将其转换为csv文件。
"""
import numpy as np
import csv
from random import randrange
from os import system

# 1 crete and save data_int.txt
list = []
for i in range(100):
    list.append(randrange(100))
print(list)

txt_file = open("data_int.txt", "w")
for element in list:
    txt_file.write(str(element) + " ")
txt_file.close()

system("cat data_int.txt")

# 5x5 floats
matrix = np.random.rand(5, 5)
txt_file2 = open("data_float.txt", "w")
for element in matrix:
    txt_file2.write(str(element) + " ")
txt_file2.close()
system("cat data_float.txt")

# txt convert to csv
with open('data_float.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('data_float.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
system("cat data_float.csv")

