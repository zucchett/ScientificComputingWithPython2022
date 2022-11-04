####### Underflow  ######

under = 1
i = 1080

for a in range(i):
    under = under / 2  
    print(a ,"     " , '%.2e' %under)
    

print(2**(-1074))
print(2**(-1075))

#######  Overflow  ######
over = 1
i = 1080

for a in range(i):
    over = over * 2
    print(a ,"     " , '%.2e' %over)

# for i = 1022 we have Overflow


    
