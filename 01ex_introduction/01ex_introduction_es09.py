#we have the limitation for "c" that it should be smaller than 100
m,n,result_list,c= 2,1,[],0
while c < 100 :
    for n in range(1,m+1):
        a = ((m**2) - (n**2))
        b = 2 * m * n
        c = ((m**2) + (n**2))
        if a == 0 or c > 100 :
            break
        else :
            result_list.append((a,b,c))
    m += 1
print(result_list)