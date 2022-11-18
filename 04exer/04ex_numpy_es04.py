#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(0,2* np.pi,100,True )
#print(n)
#extraction of every 10th element
c = np.array([n[i*9] for i in range(12)])
print("The 10th elements of the initial array are: \n",c)
#reversion of the array
d=np.array([n[-i-1] for i in range (100)])
print("The reversed array is: \n",d)
#some checks to see if the reversion succeced
for i in range(100):
    if n[i]==d[-i-1] and len(n)==len(d):
        print("Operation successfull!!!")
        break
    else:
        print("Try again!!!")
#sin and cos
#e=np.array([np.cos(n)-np.sin(n)<0.1])
#print(np.sin(n))
#print(np.cos(n))
print(np.abs(np.cos(n)-np.sin(n)))
#print(np.abs(np.cos(n)-np.sin(n))<0.1)

f = n[np.abs(np.cos(n)-np.sin(n))<0.1]
print("The elements that fullfil the condiition imposed by the problem are: \n",f)

plt.plot(n, np.sin(n))
plt.plot(n, np.cos(n))
idx = np.argwhere(np.diff(np.sign(np.cos(n) - np.sin(n)))).flatten()
plt.plot(np.cos(n)[idx], np.sin(n)[idx], 'ro')
plt.show()

