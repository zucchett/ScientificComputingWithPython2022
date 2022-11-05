#4.Counting letters


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def Occ(s):
    """Occ returns the occurence of each character in any specified string"""
    s=s.lower()
    i=0
    dic=dict()
    while i<len(s): 
        if s[i] not in dic.keys():
          c=0
          for j in s:
              if j==s[i]:
                  c=c+1
          dic[s[i]]=c
        i+=1
    return dic
print("The occurence of characters in the string s1 goes as follow:",Occ(s1))
print("The occurence of characters in the string s2 goes as follow:",Occ(s2))
