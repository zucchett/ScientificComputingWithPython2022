#Zuccolo Giada, matr. 2055702
#EXE 4
import string

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
alphabeth = list(string.ascii_lowercase)
character = [" ", ",", ";", ".", "-", "_", ":", "?", "!", "=", "(", ")", "\""]
number_list = ["0","1","2","3","4","5","6","7","8","9"]
all_lists = alphabeth + character + number_list
print("char\ts1\ts2\n--------------------")
for x in all_lists:
    print(str(x) + "\t" + str(s1.count(x)) + "\t"+ str(s2.count(x))+"\n--------------------")
