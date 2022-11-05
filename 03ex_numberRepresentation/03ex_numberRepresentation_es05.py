import math

a = 0.001
b = 1000
c = 0.001

x1_1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
x1_2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

# re-express the standard solution formula by multiplying the numerator and the denominator with (-b -+ math.sqrt(b*b - 4*a*c))
x2_1 = (2*c) / (-b - math.sqrt(b*b - 4*a*c))
x2_2 = (2*c) / (-b + math.sqrt(b*b - 4*a*c))

print("First approach,  x1 :",x1_1)
print("First approach,  x2 :",x1_2)
print("---------------------------")
print("Second approach, x1 :",x2_1)
print("Second approach, x2 :",x2_2)
print("---------------------------")

# Resluts are different. Each one of them calculates one of the roots better.
# Why?
# This is because of a dangerous operation between a large number and a small number.
# b*b is a large number and 4*a*c is a small number and operation between these two makes error, because of limitions
# of storing floating numbers.
# in first approach x ~= 0 / 2*a
# in second approach x ~= 2*c / 0
# And limitations of floating numbers would result in different outputs.
# In each approach, one of the roots would have this zero (0) and so,
# one the calculated roots that faced this zero is not completely correct.

# ------------------------------------
# Below I tried to avoid calculating 'b^2 - 4ac' because of dangerous calculation.
# I just rewrited the formula by seperating '-b/2a' and 'sqrt(b^2-4ac)/2a' and then
# taking 2a in the sqrt. It would be : sqrt{(b^2 - 4ac)/4a^2} and then : sqrt{b^2/4a^2 - 4ac/4a^2}
# which can be simpled : sqrt{(b/2a)^2 - c/a}

x3_1 = -b/(2*a) + math.sqrt((b/(2*a))**2 - c/a)
x3_2 = -b/(2*a) - math.sqrt((b/(2*a))**2 - c/a)
print("Third approach,  x1 :",x3_1)
print("Third approach,  x2 :",x3_2)