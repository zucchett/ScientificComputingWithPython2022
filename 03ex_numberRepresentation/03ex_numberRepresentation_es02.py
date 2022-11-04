# Python program to convert
# IEEE 754 floating point representation
# into real value

# Function to convert Binary
# of Mantissa to float value.
def convertToInt(mantissa_str):

	# variable to make a count
	# of negative power of 2.
	power_count = -1

	# variable to store
	# float value of mantissa.
	mantissa_int = 0

	# Iterations through binary
	# Number. Standard form of
	# Mantissa is 1.M so we have
	# 0.M therefore we are taking
	# negative powers on 2 for
	# conversion.
	for i in mantissa_str:

		# Adding converted value of
		# Binary bits in every
		# iteration to float mantissa.
		mantissa_int += (int(i) * pow(2, power_count))

		# count will decrease by 1
		# as we move toward right.
		power_count -= 1
		
	# returning mantissa in 1.M form.
	return (mantissa_int + 1)

if __name__ == "__main__":
	# Floating Point Representation
	# to be converted into real
	# value.
	ieee_32 = '1|10000000|00100000000000000000000'

	# First bit will be sign bit.
	sign_bit = int(ieee_32[0])

	# Next 8 bits will be
	# Exponent Bits in Biased
	# form.
	exponent_bias = int(ieee_32[2 : 10], 2)

	# In 32 Bit format bias
	# value is 127 so to have
	# unbiased exponent
	# subtract 127.
	exponent_unbias = exponent_bias - 127

	# Next 23 Bits will be
	# Mantissa (1.M format)
	mantissa_str = ieee_32[11 : ]

	# Function call to convert
	# 23 binary bits into
	# 1.M real no. form
	mantissa_int = convertToInt(mantissa_str)

	# The final real no. obtained
	# by sign bit, mantissa and
	# Exponent.
	real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)

	# Printing the obtained
	# Real value of floating
	# Point Representation.
	print("The float value of the given IEEE-754 representation is :",real_no)

       