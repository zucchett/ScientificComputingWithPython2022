#The derivative

########## (a) ##########
def f(x):
    return x*(x-1)

print('Derivative with the definition',(f(1+10**-2)-f(1))/10**-2)

#Analytically
def df_2(x):
    return 2*x-1

print('Derivative Analytically',df_2(1))

#The two derivatives will not agree perfectly because delta is not close enough to zero

########## (b) ##########
for delta in [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]:
    print('𝛿 =',delta,':',f(delta))
    
#the accuracy simply increase when delta decrease (delta -> 0)