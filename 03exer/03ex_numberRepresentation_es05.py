#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math

def delta(a,b,c):
    #l = []
    return [(-b-math.sqrt(b**2-4*a*c))/(2*a),(-b+math.sqrt(b**2-4*a*c))/(2*a)]

f = delta(0.001,1000,0.001)
print()
print("FIRST FUNCTION")
print(f)
print("The first solution is: ",f[0])
print("The second solution is: ","%10.25e"% f[1])

def delta2(a,b,c):

    return [((-b-math.sqrt(b**2-4*a*c)))/(2*a)*(-b+math.sqrt(b**2-4*a*c))/(-b+math.sqrt(b**2-4*a*c)),(-b+math.sqrt(b**2-4*a*c))/(2*a)*(-b-math.sqrt(b**2-4*a*c))/(-b-math.sqrt(b**2-4*a*c))]

print()
print("SECOND FUNCTION")
g=delta2(0.001,1000,0.001)
print("The first solution is: ",g[0])
print("The second solution is: ","%10.25e"% g[1])
print()
print(f[0]==g[0])
print(f[1]==g[1])
print()

print("The difference between the firsts solutions is: ",f[0]-g[0])
print("The difference between the seconds solutions is: ",f[1]-g[1])
def deltatrue(a,b,c):
    return [(-b-math.sqrt(b**2-4*a*c))/(2*a),(2*c)/(-b-math.sqrt(b**2-4*a*c))]
h = deltatrue(0.001,1000,0.001)
print()
print("CORRECT FUNCTION")
print("The first correct solution is: ",h[0])
print("The second correct solution is: ","%10.25e"% h[1])
#The results are a little bit different because of the presence of the term (-b+sqrt(delta)); in order to obtain the correct results I have to write the two solutions in terms on (-b-sqrt(delta))