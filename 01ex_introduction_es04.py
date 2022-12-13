s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1=s1.lower()
s2=s2.lower()
b=[]
c=[]
for letter in s1:
  if letter not in b:
    print(f'your text has {s1.count(letter)} {letter}')
    b.append(letter)
    for n in s2:
      if n not in c:
        print(f'your text2 has {s2.count(n)} {n}')
        c.append(n)


