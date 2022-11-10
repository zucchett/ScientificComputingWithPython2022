s1= "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2= "The quick brown fox jumps over the lazy dog"

chars_s1 , chars_s2= dict() , dict() 

for i in s1:                              
    chars_s1[i]=chars_s1.get(i,0) +1
for i in s2:
    chars_s2[i]=chars_s2.get(i,0) +1

print(f"count of Characters in S1:{chars_s1} \n")
print(f" count of Characters in S2:{chars_s2}")
