def manti_value(manti):
    power_of_two = -1
    value = 0
    for i in manti:
        value += (int(i) * pow(2, power_of_two))
        power_of_two -= 1
    return (value + 1)

def conversion_singlepre(n):
    
    sign = int(n[0])
    expo = int(n[1:9], 2)
    manti = n[10:]
    man_value = manti_value(manti)
    
    res = pow(-1, sign) * man_value * pow(2, expo - 127)
    return res

n='1101110101100001010001'
print(conversion_singlepre(n))
