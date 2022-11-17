print('######### Question 1/a #########\n')

for i in range (1,101):
    if i%3==0 and i%5!=0 :
        print("Hello")
    elif i%5==0 and i%3!=0 :
        print("World")
    elif i%5==0 and i%3==0 :
        print("HelloWorld")
    else: print(i)

print('######### Question 1/b #########\n')

l = []
for i in range (1,101):
    if i%3==0 and i%5!=0 :
        l.append("Hello")
    elif i%5==0 and i%3!=0 :
        l.append("World")
    elif i%5==0 and i%3==0 :
        l.append("HelloWorld")
    else: l.append(i)
        
myString = ' '.join(map(str,l))
myString = myString.replace("Hello","Python")
myString = myString.replace("World","Works")
l = myString.split(" ")
t = tuple(l)
print(t)