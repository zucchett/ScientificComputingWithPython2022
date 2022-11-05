s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World.\
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
charset = {}#Sets are used to store multiple items in a single variable.
for i in s1:
    chrLower = i.lower()#make all characters lowercase
    #print("charset:",charset)
    #print("charLower:",chrLower)
    #print("steps",i)
    if chrLower in charset:
        charset[chrLower] += 1 #charset[i]=charset[i]+1
    else:
        charset[chrLower] = 1
print(charset)

charset2 = {}
for k in s2:
    chrLower = k.lower()
    if chrLower in charset2:
        charset2[chrLower] += 1
    else:
        charset2[chrLower] = 1
print(charset2)