pythagoreans  = [(x,y,z) for z in range(1,100) for y in range(1,z) for x in range(1,y) if x*x + y*y == z*z]
pythagoreans = tuple(pythagoreans)
print(pythagoreans)