# The derivative

def f(a):
	return a*(a-1)
	
def df(b,exp):
	delta = 10**(-exp)
	res = (f(b+delta)-f(b))/delta
	return res

print("Derivative of x(x-1)")
x = input("Insert your x variable: ")
try:
	x = float(x)
except:
	print("Invalid input.")
	exit()

print("The derivative should be " + str(2*x-1))
print("Your calculated derivative with delta = 10^-2: " + str(df(x,2)))
print("Your calculated derivative with delta = 10^-4: " + str(df(x,4)))
print("Your calculated derivative with delta = 10^-6: " + str(df(x,6)))
print("Your calculated derivative with delta = 10^-8: " + str(df(x,8)))
print("Your calculated derivative with delta = 10^-10: " + str(df(x,10)))
print("Your calculated derivative with delta = 10^-12: " + str(df(x,12)))
print("Your calculated derivative with delta = 10^-14: " + str(df(x,14)))

# Accuracy improves consistently until 10^-6; it does improve for 10^-8 too but we can start to see some inconsistencies in the numbers. Then it's clear that df starts being unstable from 10^-10 when the accuracy starts getting worse instead of improving. We can even see an error of the order of 10^-4 for delta equal to 10^-14.
