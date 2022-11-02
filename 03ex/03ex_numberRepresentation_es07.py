# Integral of a semicircle

import math as m
import timeit as t

def f(a):
	res = m.sqrt(1-a**2)
	return res

def Rintf(N):
	integ = 0
	h = 2/N
	for i in range(N):
		xi = -1+(1/N) + i*h
		# I chose the values of x at the center of the "bin" to calculate the values of yk
		yk = f(xi)
		integ += h*yk
	return integ

print("The integral should be pi/2 = " + str(m.pi/2) + "...")
n = input("Insert number of parts to divide the function in (integer): ")
try:
	n = int(n)
except:
	print("Invalid input.")
	exit()

val100 = Rintf(100)
print("The value of the integral for N=100 is: " + str(val100))

valvar = Rintf(n)
print("The value of the integral for N=" + str(n) + " is: " + str(valvar))
print(" *The program has to re-execute the function to measure the computation time.\n  Please wait...")
time = format(t.timeit(lambda: Rintf(n), number = 1), ".6f")
print("The computation time of the integral for N=" + str(n) + " is: " + str(time) + " seconds.")

# To compute the integral in less than a second N can be increased up to ~3.4x10^6
# Running the program at values of N such that the calculations take about a minute (~2x10^8), we can calculate the value of pi/2 accurately down to the order of 10^-12
