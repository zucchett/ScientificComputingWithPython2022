"""
5. Write data to a binary file

a) Start from the data/data_000637.txt file that we have used during the previous lectures, and convert it to a binary file according to the format defined below:

from IPython.display import Image
Image("images/data_format.png")
Hints:

Read the first 10 lines using Pandas
Iterate over the DataFrame rows
For every row, ``pack'' the values (features) into a single 64-bit word, according to the format specified above. Use bit-wise shifts and operators to do so.
Write each 64-bit word to a binary file. You can use struct in this way:
binary_file.write( struct.pack('
where word is the 64-bit word.

Close the file after completing the loop.
b) Check that the binary file is correctly written by reading it with the code used in the lecture 06_OSEMN.ipynb, and verify that the content of the txt and binary files is consistent.

c) What is the difference of the size on disk between equivalent txt and binary files?
5. 将数据写入二进制文件

a) 从我们在以前的讲座中使用过的data/data_000637.txt文件开始，按照下面定义的格式将其转换为二进制文件。

从IPython.display导入Image
Image("images/data_format.png")
提示。

使用Pandas读取前10行
遍历DataFrame的行
对于每一行，根据上面指定的格式，将数值（特征）"打包 "成一个64位的字。使用位数移位和运算符来完成。
将每个64位的字写到一个二进制文件中。你可以这样使用struct。
binary_file.write( struct.pack('
其中word是64位的字。

完成循环后关闭文件。
b) 通过使用讲座06_OSEMN.ipynb中的代码读取二进制文件，检查二进制文件是否正确写入，并验证txt和二进制文件的内容是否一致。

c) 等价的txt文件和二进制文件在磁盘上的大小有什么不同？
"""