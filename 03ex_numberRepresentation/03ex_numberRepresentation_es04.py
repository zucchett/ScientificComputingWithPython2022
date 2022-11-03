a = 1.0
for i in range(0,20):
    b = a + 1.0 * 10**-i
    print("i :",i,"| %.30f:"%a,"| b :",b,"| a == b :",a==b)

# As it is shown below (after run), machine precision is less than 1e-16 and there would be no difference anymore.

# Note : %.30f or any larger number is just for diplaying number. It does not change the result and can be anything else.
# Actually a==b part is telling that if machine sees these two numbers same or not.