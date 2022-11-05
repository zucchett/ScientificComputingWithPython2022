#4. Machine precision
def Detectprecision():
    a=7.0
    b=12
    ans=0
    # Addding an increasingly small number to 7
    while(ans != a): 
        ans = a + 1.0 * 10**-b
        b+=1
        print(ans)
    print("Machin precision is: ", b-1)

Detectprecision()