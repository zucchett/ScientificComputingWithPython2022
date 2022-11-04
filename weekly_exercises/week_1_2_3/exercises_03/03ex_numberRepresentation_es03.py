#Zuccolo Giada, matr. 2055702
# EXE 3
factor = 2

print("----------------------------------------------------------------")
print("| Calculate OVERFLOW")
print("----------------------------------------------------------------")
overflow = 1
stop = False
n = 0
while not stop:
    try:
        overflow = overflow * factor
        if n<1000:
            print("> ", "%2d" % n, "\t\t\t", "%2.8e" % overflow)
        else:
            print("> ", "%2d" % n, "\t\t", "%2.8e" % overflow)
        n += 1
        stopOver = n, "%2.8e" % (overflow)
    except:
        stop = True

print("----------------------------------------------------------------")
print("| Calculate UNDERFLOW")
print("----------------------------------------------------------------")
underflow = 1
n = 0
stop_val = 0.00000e+00
while underflow!=stop_val:
    underflow = underflow / factor
    if underflow!=stop_val:
        if n < 1000:
            print("> ", "%2d" % n, "\t\t\t", "%2.8e" % underflow)
        else:
            print("> ", "%2d" % n, "\t\t", "%2.8e" % underflow)
        n += 1
        stopUnder = n, "%2.8e" % (underflow)

print("\n----------------------------------------------------------------")
print("| RESUME")
print("----------------------------------------------------------------")
print("> OVERFLOW\nn = "+str(stopOver[0])+" \t value = "+str(stopOver[1]))
print("\n> UNDERFLOW\nn = " + str(stopUnder[0]) + " \t value = " + str(stopUnder[1]))