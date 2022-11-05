s1="Write a program that prints the numbers from 1 to 100. \But for multiples of three print Hello instead of the number and for the multiples of five print World. \For numbers which are multiples of both three and five print HelloWorld."
s2="The quick brown fox jumps over the lazy dog"
s1_l=list(s1.lower())
s2_l=list(s2.lower())
i=0
j=0
list1=[]
list2=[]
print("Stringa 1:")
while i<len(s1_l):
	char=s1_l[i]
	if char not in list1:
		print(char,":",s1_l.count(char))
		list1.append(char)
	i=i+1
print("Stringa 2:")
i=0
while i<len(s2_l):
        char=s2_l[i]
        if char not in list2:
                print(char,":",s2_l.count(char))
                list2.append(char)
        i=i+1
