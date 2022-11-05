#6/The derivative

f=lambda x: x*(x-1)

#a
def deriv(x):
    gamma=0.01
    return ( f(x+gamma)-f(x) ) / gamma

f_1=deriv(1)
print("The derivative of the function at x=1 using the derivative definition is: ",f_1)

#the true derivative analytically: f'=2*x-1
f_1= 2*1-1
print("The true value of the same derivative analytically is: ",f_1)
#The two result are slightly diffrent but very close.
#This is due to how stable the function deriv is 


#b
gamma =0.0001
while gamma >=10**(-14):
    print( (f(1+gamma)-f(1)) / gamma )
    gamma*=0.01
#The results show that while decreasing gamma to 10exp-8 The result gets even closer to the real value.
    #And decreasing gamma even more will make the result a little far from the real result
