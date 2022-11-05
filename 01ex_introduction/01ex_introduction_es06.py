x=input("x = ")
y=input("y = ")
try:
	x=float(x)
	if(x%1==0):
       		x=int(x)
	y=float(y)
	if(y%1==0):
        	y=int(y)
	sum=x+y
	print("x+y=", sum)
except:
	print("Valori inseriti non compatibili")


