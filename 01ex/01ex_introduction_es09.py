# Nested list comprehension
import math as m

a = 1;
b = 1;
c = m.sqrt(a**2 + b**2)

l = ();

for a in range (11):	# Because sqrt(100) = 10, going above it becomes repetitive
	if a != 0:
		while c < 100:
			try:
				if c - int(c) == 0:	# Test if c is an integer
					l += ((a,b,int(c)),)
			except:
				pass
			b += 1
			c = m.sqrt(a**2 + b**2)
		b = a
		c = m.sqrt(a**2 + b**2)
# I fixed the "a" value and I increased "b" until the obtained "c" exceeds 100, then I raised the value of "a" by a unit and restarted the loop over the "b" until it exceeds 100...
	
print(str(l))
