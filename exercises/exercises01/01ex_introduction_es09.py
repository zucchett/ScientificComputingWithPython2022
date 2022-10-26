pyth_trip_list = ()

for a in range(1, 100):
    for b in range(a, 100):
        for c in range(b, 100):
            if (pow(a,2)+pow(b,2)) == (pow(c,2)):
                temp = (a,b,c)
                pyth_trip_list = pyth_trip_list+(temp,)

print(pyth_trip_list)