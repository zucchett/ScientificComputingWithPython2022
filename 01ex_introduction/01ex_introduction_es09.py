def pythagoreanTriplets(limit=100) :
    c, m = 0, 2
    list1=[ ]
    while c < limit :
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            if c > limit :
                break
            
            list1.append(a)
            list1.append(b)
            list1.append(c)
        m = m + 1
        
    to_tup = tuple(list1)
    print(type(to_tup))
    print(to_tup)


pythagoreanTriplets()