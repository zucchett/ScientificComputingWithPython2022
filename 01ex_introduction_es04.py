s1= ("Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld.").lower()
s2= ("The quick brown fox jumps over the lazy dog").lower()
count_s1 , count_s2= dict() , dict()
for i in s1:
    count_s1[i]=count_s1.get(i,0) +1
for i in s2:
    count_s2[i]=count_s2.get(i,0) +1

print(f"\nCount of S1:\n{count_s1} \n\nCount of S2:\n{count_s2}\n")
