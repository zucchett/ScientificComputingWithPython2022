import math
import sys

def convertNum(n,t):
	if isinstance(n,int)==0:
		st=str(n)
		try:
			n=int(st,2)
		except:
			n=int(st,16)
	if t=="bin":
		return bin(n)
	if t=="hex":
		return hex(n)
	if t=="dec":
		return n
	else:
		print("Invalid output type")
a=12
b=convertNum(a,"hex")
print(b)
c=convertNum(a,"bin")
print(c)
d=bin(a)
e=convertNum(d,"dec")
print(e)
