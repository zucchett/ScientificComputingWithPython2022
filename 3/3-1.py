def N_Rep(a):
        if a[-len(a)+1] == 'b' :
            D = int(a,2)
            H = hex(D)
            B = a
            return D,H,B
        elif  a[-len(a)+1] == 'x' :
            D = int(a,16)
            B = bin(D)
            H = a
            return D,H,B
        else :
            D = int(a)
            B = bin(D)
            H = hex(D)
            return D,H,B
    
Input_= input('your Num : ')
N_Rep(Input_)