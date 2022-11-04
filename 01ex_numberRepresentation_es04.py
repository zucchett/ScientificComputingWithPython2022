s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

import numpy as np




def count_char(s):
	s = s.lower()
	counter = np.zeros(26)

	for ch in s:
    		if 'a' <= ch <= 'z':   
        		counter[ord(ch) - ord('a')] += 1

	for i in range(0, 26):
    		print(chr(i+ord('a')),' repeated', int(counter[i]) ,'times')


print('number of repeated characters in s1:')
count_char(s1)
print('\nnumber of repeated characters in s2:') 
count_char(s2)



