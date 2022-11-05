#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
a1 = input("First variable: ")
a2 = input("Second variable: ")


try:
    a1 = int(a1)      
except:
    try:
        a1 = float(a1)
    except:
        pass


try:
    a2 = int(a2)
except:
    try:
        a2 = float(a2)
    except:
        pass

print("type(a1) = "+ str(type(a1))) 
print("type(a2) = " + str(type(a2)))


try:
    sum = a1 +a2
    print("The sum is: " + str(sum))
except:
    print("The sum is not possible") 
    


