s1= "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2= "The quick brown fox jumps over the lazy dog"
count_s1 , count_s2= dict() , dict()
for q in s1:
    count_s1[q]=count_s1.get(q,0) +1
for q in s2:
    count_s2[q]=count_s2.get(q,0) +1
print(f"Count of S1:\n{count_s1} \n\nCount of S2:\n{count_s2}")
