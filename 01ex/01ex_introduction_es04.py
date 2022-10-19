# Counting letters

from string import ascii_lowercase as alf

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

freq1 = {}
freq2 = {}

for chrctr in s1.lower():
	if chrctr in freq1:
		freq1[chrctr] += 1
	else:
		freq1[chrctr] = 1
	

for chrctr in s2.lower():
	if chrctr in freq2:
		freq2[chrctr] += 1
	else:
		freq2[chrctr] = 1
		
print("String s1: \n" + str(freq1))
print("String s2: \n" + str(freq2))
