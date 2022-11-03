import math

def ieee754(str):
	sign=str[0]
	exp=str[1:9]
	man=str[9:]
	try:
		exp=int('0b'+exp,2)
	except:
		raise Exception("Please insert a binary string (exponent not valid)")
	try:
		man_check=int('0b'+man,2)
	except:
		raise Exception("Please insert a binary string (mantissa not valid)")
	if sign=='0' and exp==255 and man_check==0:
		return inf
	if sign=='1' and exp==255 and man_check==0:
		return -inf
	elif exp==255 and man_check>0:
		return float('nan')
	else:
		exp=exp-127
		f=1
		for i in range(23):
			f=f+int(man[i])/(2**(i+1))
		if sign=='0':
			return f*(2**exp)
		if sign=='1':
			return -f*(2**exp)
		else:
			raise Exception("Sign is not valid")
ie='11000010101100000000000000000000'
print(ieee754(ie))
