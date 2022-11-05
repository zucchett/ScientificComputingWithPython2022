
# 4. Trigonometric functions

# Use np.linspace to create an array of 100 numbers between  and  (inclusive).

# Extract every 10th element using the slice notation
# Reverse the array using the slice notation
# Extract elements where the absolute difference between the sin and cos functions evaluated for that element is 
# Optional: make a plot showing the sin and cos functions and indicate where they are close

# -------------------------------------- Code Begin-------------------------------------
import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, 2* np.pi, num = 100)

print('Array of 100 number between 0 and  2 pi : \n ', u)
print('\n ------------------------------------------- \n')
print('Extracting every 10th element : ', u[0::10])
print('\n ------------------------------------------- \n')
print('Reversing the array using the slice notation : \n', u[::-1])
print('\n ------------------------------------------- \n')

mask = np.abs(np.sin(u) - np.cos(u)) < 0.1
print('Elements where the absolute difference between the sin and cos functions evaluated for that element is < 0.1 : \n', u[mask] )

plt.figure(figsize=(10, 10))
plt.plot(u, np.sin(u))
plt.plot(u, np.cos(u))
plt.ylabel('Sin & cos')


# -------------------------------------- Code End---------------------------------------
