s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()
freq_char_s1 = {}
freq_char_s2 = {}
  
for i in s1:
    if i in freq_char_s1:
        freq_char_s1[i] += 1 
    else:
        freq_char_s1[i] = 1 
print (str(freq_char_s1) + '\n')

for j in s2:
    if j in freq_char_s2:
        freq_char_s2[j] += 1 
    else:
        freq_char_s2[j] = 1 
print (str(freq_char_s2))