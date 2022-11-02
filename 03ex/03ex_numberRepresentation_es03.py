# Underflow and overflow

import struct as st

def binary(n):
	aux = st.pack('>d', n).hex()
	baux = bin(int(aux, 16))
	baux = baux.replace("0b","")
	return int(baux,2)

over = 1.
under = 1.

while type(over) is float:
	overt = over * 2
	print(over)
	if overt == 2*overt:
		break
	else:
		over = overt
# Exploited Overflow -> Converted to Infinity

print("-----------------------------------------------")

while type(under) is float:
	undert = under / 2
	underf = binary(undert)
	print(under)
	
	# Exponent
	mask = 9218868437227405312
	shift = 52
	exp = (underf & mask) >> shift
	if exp == 0:
		break
	else:
		under = undert
# Exploited Underflow -> Subnormal numbers, so exponent in double is 0

print("Overflow limit of this PC is " + str(over) + " within a 2 factor.")
print("Underflow limit of this PC is " + str(under) + " within a 2 factor.")
