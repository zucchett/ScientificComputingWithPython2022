"""
4. Reading the credit card numbers

Get the binary file named credit_card.dat from this address:

https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat
and convert the data into the real credit card number, knowing that:

each line corresponds to a credit card number, which consists of 16 characters (which are numbers in the 0-9 range) divided in 4 blocks, with a whitespace between each block
each character is written using a 6 bit binary representation (including the whitespace)
the final 4 bits of each line are a padding used to determine the end of the line, and can be ignored
Hint: convert the binary numbers to the decimal representation first, and then use the chr() function to convert the latter to a char
4. 读取信用卡号码

从这个地址获取名为credit_card.dat的二进制文件。

https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat
并将数据转换成真正的信用卡号码，要知道。

每一行对应一个信用卡号码，由16个字符组成（这些字符是0-9范围内的数字），分为4个区块，每个区块之间有一个空白区
每个字符用6位二进制表示（包括空白处）。
每行的最后4位是用于确定该行结束的填充，可以忽略不计。
提示：首先将二进制数字转换为十进制表示，然后使用chr()函数将后者转换为一个字符

"""