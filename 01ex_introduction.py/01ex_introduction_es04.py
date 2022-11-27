
# 4. Counting sring
from collections import Counter 
s = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld.".lower()

#string_op = [s for s in string]

count1 = {x : s.count(x) for x in set(s)}

print("The counted words" +str(count1))