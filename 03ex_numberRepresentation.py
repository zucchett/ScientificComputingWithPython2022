# 03ex_numberRepresentation by Alberto Merotto 208117
#*************************************************************
#Exercise 01:
import sys
def bdx_converter(v, t):
	if(type(v) == type(1)): #if input value v is an integer then it can be converted in bin or hex
		if(t=='b'):
			return bin(v)
	
		elif(t=='x'):
			return hex(v)
		
		else:
			print('wrong conversion parameter identifier')
	
	elif(type(v)==type('s')): #if v is a string then it could be an hex or a bin or something else (wrong)
		if(t=='d'):
			try:
				if v[1] == 'x':
					return int(v, 16)
				elif v[1] == 'b':
					return int(v, 2)
				else:
					print('invalid input string!')
			except ValueError:
				print('invalid input string!')
		elif(t=='b'):
			try:
				if v[1] == 'x':
					return bin(int(v, 16))
				elif v[1] == 'b':
					return bin(int(v, 2))
				else:
					print('invalid input string!')
			except ValueError:
				print('invalid input string!')
		elif(t=='x'):
			try:
				if v[1] == 'x':
					return hex(int(v, 16))
				elif v[1] == 'b':
					return hex(int(v, 2))
				else:
					print('invalid input string!')
			except ValueError:
				print('invalid input string!')
		else:
			print('wrong conversion parameter identifier')
	else:
		print('Wrong Input')
		
a = 23
b = 'hello'
c = 3.14
d = '_b_tricky'


print('test with: ')
print(a)
print(bdx_converter(a, 'x'))
print(bdx_converter(a, 'b'))
print(bdx_converter(a, 'd'))
print('******************************************')

print('test with: ')
print(b)
print(bdx_converter(b, 'x'))
print(bdx_converter(b, 'b'))
print(bdx_converter(b, 'd'))
print('******************************************')

print('test with: ')
print(c)
print(bdx_converter(c, 'x'))
print(bdx_converter(c, 'b'))
print(bdx_converter(c, 'd'))
print('******************************************')

print('test with: ')
print(d)
print(bdx_converter(d, 'x'))
print(bdx_converter(d, 'b'))
print(bdx_converter(d, 'd'))
print('******************************************')

print('test with: ')
print(hex(a))
print(bdx_converter(hex(a), 'x'))
print(bdx_converter(hex(a), 'b'))
print(bdx_converter(hex(a), 'd'))

print('******************************************')

print('test with: ')
print(bin(a))
print(bdx_converter(bin(a), 'x'))
print(bdx_converter(bin(a), 'b'))
print(bdx_converter(bin(a), 'd'))

#*************************************************************
#Exercise 02:
def fpn(n):
	n = str(n) #casting to be sure
	#checks if the input is correct
	if len(n) != 32:
		print('Invalid input! Accepting only 32 character long input string')
		return
		
	for i in range(len(n)):
		if (n[i] != '0' and n[i] != '1'):
			print('Invalid Input! Input String must contains only 0s and 1s')
			return
	#parsing the exponent	
	exp = '0b'
	for i in range(1, 9):
		exp = exp + str(n[i])
	
	exp = int(exp, 2)
	#parsing the mantissa
	man = ''
	for i in range(9, 32):
		man = man + str(n[i])
	
	mnt = 1
	for j in range(23):
		if man[j] == '1':
			mnt = mnt + (1/2**(j+1))
	
	#computing the result	
	r = (mnt) * 2**(exp - 127)
	if(n[0] == '1'): 	#checks sign bit
		r = r * (-1)
	return r
	
	
n1 = 11000010101100000000000000110101
n2 = '01010010100100010001000000110100'
n3 = '01000010100010110010001100101111'

 
print(fpn(n1))
print(fpn(n2))
print(fpn(n3))

print(fpn('11000020101100000000000000110101'))
print(fpn('hello world'))

#*************************************************************
#Exercise 03:
def ex03():
	steps = 1500
	underflow = 1
	overflow = 1
	for n in range(steps):
		underflow = underflow/2  #after 1073 step the underflow can be detected at the value 4.94066e-324
		overflow = overflow*2	 #after 1022 steps the OverFlowError exception is launched and the value is 8.98847e+307 
		print('|%2d'%n, '\t\t', '|%2.5e'%underflow, '|', '\t\t','%2.5e'%overflow, '|')

#ex03()
	
#*************************************************************
#Exercise 04:
def ex04():	
	steps = 300000000
	v = 1
	overflow = 1
	l = []
	l.append(v)
	for n in range(steps):
		v = v + 1/((n+1)**2)
		print('|%2d'%n, '\t\t', '|%2.5e'%v, '|')
		if(l[0] == v):
			print('limit reached at', 1/((n+1)**2)) #the limit is reached at 2.220446049250313e-16
			break
		l.clear()
		l.append(v)
#ex04()

#*************************************************************
#Exercise 05:
import math
def quadratic_solution(a, b, c):
	if(a==0):
		print('a cannot be zero')
		return
	try:
		x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(a*2)
		x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(a*2)
		print('x1= ', x1, 'x2= ', x2)
	except ValueError:
		print('cannot compute imaginary numbers')
		return

quadratic_solution(0.001,1000,0.001)
quadratic_solution(1,2,1)

def quadratic_solution_v2(a, b, c):
	if(a==0):
		print('a cannot be zero')
		return
	try:
		x1 = ((-b + math.sqrt((b**2)-(4*a*c)))*(-b - math.sqrt((b**2)-(4*a*c))))/((a*2)*(-b - math.sqrt((b**2)-(4*a*c))))
		x2 = ((-b - math.sqrt((b**2)-(4*a*c)))*(-b + math.sqrt((b**2)-(4*a*c))))/((a*2)*(-b + math.sqrt((b**2)-(4*a*c))))
		print('x1= ', x1, 'x2= ', x2)
	except ValueError:
		print('cannot compute imaginary numbers')
		return
		
quadratic_solution_v2(0.001,1000,0.001)
#in this case the value of the first root is the same, while the value of the second root has a bit more precision since it is equal to -999999.9999990001 instead of -999999.999999. This is because values variations are so small that the precision of the computer is not enough


def quadratic_solution_v3(a, b, c):
	delta = b**2 - 4*a*c 
	sqrtval = math.sqrt(abs(delta)) 
	if delta > 0:
		print(" real and different roots ") 
		print((-b + sqrtval)/(2 * a)) 
		print((-b - sqrtval)/(2 * a)) 
	elif delta == 0:
		print(" real and same roots") 
		print(-y / (2 * x)) 
	else:
		print("Complex Roots") 
		print(- b / (2 * a), " + i", (sqrtval)/(2*a)) 
		print(- b / (2 * a), " - i", (sqrtval)/(2*a)) 

quadratic_solution_v3(0.001,1000,0.001)
quadratic_solution_v3(1,1,1)

#*************************************************************
#Exercise 06:

def funct(x):
	return x*(x-1)

x=1
l = [-2, -4, -6, -8, -10, -12, -14, -16]
for e in l:
	d = 10**(e)

	derivative = (funct(x+d)-funct(x))/(d)
	print(e, derivative)

#best accuracy is for delta = 10**(-10), for bigger values the value of the derivative is overestimated, while with smaller values like delta = 10**(-16) it degenerates to zero


#*************************************************************
#Exercise 07:


