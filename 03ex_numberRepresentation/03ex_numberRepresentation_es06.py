# 6. The derivative

# Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1) 
# (a) Calculate the derivative of the function at the point  𝑥=1
# using the derivative definition:

# d𝑓d𝑥=lim𝛿→0𝑓(𝑥+𝛿)−𝑓(𝑥)𝛿
 
# with  𝛿=10−2 . Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?

# (b) Repeat the calculation for  𝛿=10−4,10−6,10−8,10−10,10−12  and  10−14 . How does the ac
# curacy scale with  𝛿 ?

# -------------------------------------- Code Begin-------------------------------------

print('----------------------- Question a ---------------------')

f = lambda x : x*(x-1)
derivative = lambda d : (f(1+d)-f(1))/d

print("the derivative of the function f at the point  𝑥=1 is : ", derivative(0.01))
# The Analitical derivative is 1
# The computed derivative is 1.010 -- > which is different from the analitical derivative
# Because the in forumla the delta approaches continually to the value of 0, Unlike the computed derivative which is given a dicrete value of
# delta and it's not close enough to zero
# So, The more delta get smaller ( closer to zero) the more the results are more accurate 
print('----------------------- Question a ---------------------')

l = [10**-4, 10**-6,10**-8,10**-8,10**-10,10**-12,10**-14]
for i in l:
    print("The derivative of f with delta = ", i ," at 𝑥=1 is : ", derivative(i))

# So, The more delta get smaller ( closer to zero) the more the results are more accurate 

# -------------------------------------- Code End  -------------------------------------
