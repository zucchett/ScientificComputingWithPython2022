def DetectPrecision():
    a = 8.0
    b = 16
    ans = 0

    while(ans != a):
        ans = a + 1.0 * 10**-b
        b += 1
        print(ans)
    print("Machine Precision is: ", b-1)    

DetectPrecision()    