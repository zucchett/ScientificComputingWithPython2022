# Prime numbers sieve

import numpy as np
import math as m
import timeit as t

def prime(N):
	a = np.arange(0, N)
	mask = np.full((N,), True)
	for i in range(m.ceil(m.sqrt(N))): # Up to sqrt(N) to avoid redundancy
		if i < 2:
			mask[i] = False
		elif i >= 2:
			for j in a:
				if a[j] % i == 0 and a[j] != i: # Multiples of n == x%n = 0
					mask[j] = False
	afil = a[mask]
	return afil

def eratosthenes(N):
	a = np.arange(0, N)
	mask = np.full((N,), True)
	for i in range(m.ceil(m.sqrt(N))): # Up to sqrt(N) to avoid redundancy
		if i < 2:
			mask[i] = False
		elif i >= 2:
			if mask[i] == True: # Eratosthenes optimisation, not over every number
				for j in a:
					if a[j] % i == 0 and a[j] != i: # Multiples of n == x%n = 0
						mask[j] = False
	afil = a[mask]
	return afil


# Input + Check
n = input("Insert integer N: ")

try:
	n = int(n)
except:
	print("N is not an integer.")
	exit()

# Choose computation method
meth = input("Choose computation method (non-optimised: \"n\", Eratosthenes: \"e\"): ")

if meth.lower() == ("n"):

	# Function call
	pr = prime(n)
	
	print("List of prime numbers up to N:")
	print(str(pr) + "\n")
	
	proceed = input("Measure computational time? (y/n): ")
	
	if proceed.lower() == ("y" or "yes"):
	
		print(" *The program has to re-execute the function to measure the computation time.\n  Please wait...\n")
		timep = format(t.timeit(lambda: prime(n), number = 1), ".6f")
	
		print("Computational time (non-optimised): " + timep + " seconds")
		print("\n Considering the non-optimised method, at low N the iteration time over the loops is still comparable with the array initialisation time and effects of fluctuations are still relevant, so it has an erratic behaviour.")
		print(" In theory at increasing N value the computational time should be proportional to the product of the 2 ranges the program is looping over since it's the dominant process in the program. Therefore it should be approximately proportional to N^(3/2) (N x N^(1/2)).")
		print(" In reality I do not obtain an exact proportionality with N^(3/2), but a function that rises slightly slower (resulting in a calculation which is faster than expectations).\n")
		
		print("Ratio computational time/N^(3/2): " + str(format(float(timep)/(n**(3/2)), ".4g")))

# Actually I did have good proportionality relation before adding the eratosthenes part of the code, since I basically obtained values of the ratios which changed within 10% over an order of magnitude. Now it is not as constant, since it keeps going down faster increasing N. Does it have anything to do with memory management? By the way I tried using N = 100, 1000, 10000, 100000, 1000000
	
	elif proceed.lower() == ("n" or "no"):
		exit()
	
	else:
		print("I take that as a no.")
		exit()

elif meth.lower() == ("e"):

	# Function call
	pr = eratosthenes(n)
	
	print("List of prime numbers up to N:")
	print(str(pr) + "\n")
	
	proceed = input("Measure computational time? (y/n): ")
	
	if proceed.lower() == ("y" or "yes"):
	
		print(" *The program has to re-execute the function to measure the computation time.\n  Please wait...\n")
		timee = format(t.timeit(lambda: eratosthenes(n), number = 1), ".6f")
	
		print("Computational time (Eratosthenes): " + timee + " seconds")
		print("\n Considering the Eratosthenes optimised method, the program is not looping over every single number to determine the multiples, but only over the prime numbers.")
		print(" Therefore (at large values of N) the proportionality should not be N x N^(1/2) anymore, but instead N x k x N^(1/2), where k is the fraction of prime numbers up to the number N (so k is not a constant). This should result in a relation of the type kN^(3/2) with k<1.")
		print(" In reality I do not obtain an exact proportionality with kN^(3/2), but a function that rises slightly slower (resulting in a calculation which is faster than expectations).\n")
		
		# Comparing the behaviour of the Eratosthenes ratio for increasing N value with the behaviour of the non-optimised ratio they look very similar, since they are reduced by about a factor 2 for every order of magnitude, except for the 10^6 to 10^7 step where they both suddently don't reduce as much. So either this behaviour is related to the same mechanism in the algorithm or I am simply making a big mistake somewhere which affects both the functions.
		
		k = len(list(pr))/n
		print("Fraction of prime numbers up to N: " + str(k))
		print("Ratio computational time/kN^(3/2): " + str(format(float(timee)/(k*n**(3/2)), ".4g")))
	
	elif proceed.lower() == ("n" or "no"):
		exit()
	
	else:
		print("I take that as a no.")
		exit()

else:
	print("Invalid input.")
	exit()
