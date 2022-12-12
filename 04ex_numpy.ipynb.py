import numpy as np
import math
import matplotlib.pyplot as plt

array = np.linspace(0,2*math.pi,100)
print(array)

#extract every 10th element using slice notation
new_array = array[::10]
print("\n The elements that are in the 10th:\n",new_array)

#reverse the array using slice notation
reverse_new_array =new_array[::-1] 
print("\n Reversed elements that are in the 10th:\n",reverse_new_array)

#extract elements where the abs. difference between sin and cos functions evaluated for that element is <0.1
#print(reverse_new_array[0])
x_x = np.abs(np.sin(array)-np.cos(array)) < 0.1
print("\nExtracted elemens in array:","\n",array[x_x])

#Optional: make a plot showing the sin and cos functions and indicate where they are close
plt.scatter(array[x_x], np.sin(array[x_x]))
plt.plot(array, np.sin(array), array, np.cos(array))