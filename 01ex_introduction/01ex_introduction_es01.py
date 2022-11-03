import math
c=1
l=[]
while(c<=100):
	if(c%3==0 and c%5==0):
		print("HelloWorld")
		l.append("HelloWorld")
	elif(c%3==0):
		print("Hello")
		l.append("Python")
	elif(c%5==0):
		print("World")
		l.append("Works")
	else:
		print(c)
		l.append(c)
	c=c+1
print("")
print("Now I print the tuple:")
t=tuple(l)
print(t)
