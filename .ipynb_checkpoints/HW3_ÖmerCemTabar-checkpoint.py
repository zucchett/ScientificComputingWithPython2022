"""
Author : Ömer Cem Tabar
Exercise Document 02 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
## Q1 - Number Representation
"""

def BinaryChecker(x):
    try:
        val = int(x,2)
        return True
    except:
        return False

def HexadecimalChecker(x):
    try:
        if x[0] == '0' and x[1] == 'x':
            val = int(x,16)
            return True
        else:
            return False
    except:
        return False
    
def NumberConvertion(inputValue,outputType):
    #Given that there is an input that is either bin/hex/dec
    #Given that there is a dedicated output type
    #Post => Turn the input into dedicated type and return
    
    if BinaryChecker(inputValue) == True: #number is binary
        if outputType == 'dec':
            return int(inputValue,2)
        elif outputType == 'hex':
            integer = int(inputValue,2)
            i = hex(integer)
            return i
        else:
            return inputValue
    
    else: #number is decimal or hexadecimal
        if HexadecimalChecker(inputValue) == True: #number is hexadecimal
            if outputType == 'dec':
                return int(inputValue,16)
            elif outputType == 'hex':
                return inputValue
            else:
                integer = int(inputValue,16)
                return bin(integer)
        else: #number is decimal
            x = int(inputValue)
            if outputType == 'dec':
                return x
            elif outputType == 'hex':
                return hex(x)
            else:
                return bin(x)

inpt = input("Please enter an input value:")
outTyp = input("Please enter an output type for conversion (either write dec/hex/bin):")
print(NumberConvertion(inpt, outTyp))           





#Please be aware that I specified the required input in order to define the outputType
#For binary a user must enter 'bin', for decimal 'dec' and for hexadecimal 'hex'notation should be entered


"""

print("INPUT","\t\t\t","OUTPUT", "\t\t\t")
print("-------------------------------------------------------------------------------------")
print(67131,"\t\t\t", NumberConvertion(67131, "hex"), "\t\t\t", "Decimal to Hexadecimal Convertion")
print(67131,"\t\t\t", NumberConvertion(67131, "dec"), "\t\t\t\t", "Decimal to Decimal Convertion")
print(67131,"\t\t\t", NumberConvertion(67131, "bin"), "\t\t", "Decimal to Binary Convertion")
print("-------------------------------------------------------------------------------------")

print("0b10000011000111011","\t", NumberConvertion("0b10000011000111011", "hex"), "\t\t\t", "Binary to Hexadecimal Convertion")
print("0b10000011000111011","\t", NumberConvertion("0b10000011000111011", "dec"), "\t\t\t\t", "Binary to Decimal Convertion")
print("0b10000011000111011","\t", NumberConvertion("0b10000011000111011", "bin"), "\t\t", "Binary to Binary Convertion")
print("-------------------------------------------------------------------------------------")

print("0x1063b","\t\t", NumberConvertion("0x1063b", "hex"), "\t\t\t", "Hexadecimal to Hexadecimal Convertion")
print("0x1063b","\t\t", NumberConvertion("0x1063b", "dec"), "\t\t\t\t", "Hexadecimal to Decimal Convertion")
print("0x1063b","\t\t", NumberConvertion("0x1063b", "bin"), "\t\t", "Hexadecimal to Binary Convertion")
print("-------------------------------------------------------------------------------------")
"""



#Please be aware that I specified the required input in order to define the outputType
#For binary a user must enter 'bin', for decimal 'dec' and for hexadecimal 'hex'notation should be entered


"""
## Q2 - 32bit Floating Number
"""

first_example = "11000010101100000000000000000000"
second_example = "00000011111000000000000000000000"
third_example = "11000000101100000000000000000000"
def SinglePrecisionConvertion(binaryNumber):
    signBit = binaryNumber[0]
    exponent = binaryNumber[1:9]
    fraction = binaryNumber[9:len(binaryNumber)]
    if signBit == '0': #It means converted decimal number will be positive
        new_exponent = exponent[::-1]
        exponent_sum = 0
        fractional_sum = 0
        for i in range(0,len(new_exponent)):
            exponent_sum += (int(new_exponent[i]) * (2**(i)))
        for i in range(0,len(fraction)):
            fractional_sum += (int(fraction[i]) * (2**(-(i+1))))
        singlePrecisionalTranslation = (1 + fractional_sum) * (2**(exponent_sum - 127))
        return(singlePrecisionalTranslation)
    else: #It means converted decimal number will be negative
        new_exponent = exponent[::-1]
        exponent_sum = 0
        fractional_sum = 0
        for i in range(0,len(new_exponent)):
            exponent_sum += (int(new_exponent[i]) * (2**(i)))
        for i in range(0,len(fraction)):
            fractional_sum += (int(fraction[i]) * (2**(-(i+1))))
        singlePrecisionalTranslation = (-(1 + fractional_sum)) * (2**(exponent_sum - 127))
        return(singlePrecisionalTranslation)

first = SinglePrecisionConvertion(first_example)
second = SinglePrecisionConvertion(second_example)
third = SinglePrecisionConvertion(third_example)
print("Result of the first example:" + str(first))
print("Result of the second example:" + str(second))
print("Result of the third example:" + str(third))


"""
## Q3 - Underflow and Overflow

"""

def OverflowDetection():
    print("\t\t", "OVERFLOW DETECTION", "\t\t\t")
    print("----------------------------------------")
    overflow = 1  #multiply the overflow number with factor 2 repeatedly until my computer can not handle the number anymore
    #As given in the hint, in order to halve and multiply the numbers lets define a factor as '2'
    factor = 2
    #To be sufficient lets set an N number, and change accordingly in order to detect calculation error
    for i in range(1300):
        overflow = overflow*factor
        print("%2d"%i, "\t\t\t", "%2.5e"%overflow)
        print("------------------------------------")
        
def UnderflowDetection():
    print("\t\t", "UNDERFLOW DETECTION", "\t\t\t")
    print("----------------------------------------")
    #minimum number case
    underflow = 1 #divide the underflow number with factor 2 repeatedly until my computer can not handle the number anymore
    factor = 2
    #To be sufficient lets set an N number, and change accordingly in order to detect calculation error
    for i in range(1500):
        underflow = underflow/2
        print("%2d"%i, "\t\t\t", "%2.5e"%underflow)
        print("------------------------------------")  

OverflowDetection()
#At the point 1023 (index 1022) we obtained the overflow limit.
UnderflowDetection()
#At the point 1075 (index 1074)  we obtained the underflow limit.

"""
## Q4 - Machine Precision
"""
def MachinePrecision():
    baseNumber = 1
    addNumber = 2
    for i in range(60):
        baseNumber += addNumber
        addNumber = addNumber / 2
        print(str(i), "\t\t\t", str(baseNumber))
        print("--------------------------------------------")
MachinePrecision()

print("-----------------------------------------------")
print("After 52th (index 51) addition, there will no effect on the base number since added number is nearly equal to 0")
print("The resultant number will stop at 5.0 and there will no observative changes later on (starting point was 1)")

"""
## Q5 - Quadratic Solution Part(a)
"""

import math as m
def QuadraticSolutions(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1,x2

x1,x2 = QuadraticSolutions(0.001,1000,0.001)
print("First solution is: ",  x1 , " and the second solution is: ", x2 ,".")

"""
## Q5 - Quadratic Solution Part(b)
"""

def QuadraticSolutionsModified(a,b,c):
    #multiply nominator and denominator with ((-b) + m.sqrt((b**2) - ((4*a)*c)))
    x11 = ((((-b) + m.sqrt((b**2) - ((4*a)*c))) * ((-b) + m.sqrt((b**2) - ((4*a)*c)))) / ((2*a)*((-b) + m.sqrt((b**2) - ((4*a)*c)))))
    #multiply nominator and denominator with ((-b) - m.sqrt((b**2) - ((4*a)*c)))
    x12 = ((((-b) + m.sqrt((b**2) - ((4*a)*c))) * ((-b) - m.sqrt((b**2) - ((4*a)*c)))) / ((2*a)*((-b) - m.sqrt((b**2) - ((4*a)*c)))))
    #multiply nominator and denominator with ((-b) + m.sqrt((b**2) - ((4*a)*c)))
    x21 = ((((-b) - m.sqrt((b**2) - ((4*a)*c))) * ((-b) + m.sqrt((b**2) - ((4*a)*c)))) / ((2*a)*((-b) + m.sqrt((b**2) - ((4*a)*c)))))
    #multiply nominator and denominator with ((-b) - m.sqrt((b**2) - ((4*a)*c)))
    x22 = ((((-b) - m.sqrt((b**2) - ((4*a)*c))) * ((-b) - m.sqrt((b**2) - ((4*a)*c)))) / ((2*a)*((-b) - m.sqrt((b**2) - ((4*a)*c)))))
    
    return x11,x12,x21,x22
x11,x12,x21,x22 = QuadraticSolutionsModified(0.001,1000,0.001)
print("First solution is: " + str(x11) + " and the second solution is: " + str(x12) + ".")
print("Third solution is: " + str(x21) + " and the fourth solution is: " + str(x22) + ".")

#There is no suspicious change in three cases:
## -b-(√b^2-4ac)/2a multiplying nominator and denominator with -b-√b^2-4ac/2a
## -b+(√b^2-4ac)/2a multiplying nominator and denominator with -b-√b^2-4ac/2a
## -b+(√b^2-4ac)/2a multiplying nominator and denominator with -b-√b^2-4ac/2a
#However, in the case of -b-(√b^2-4ac)/2a multiplying nominator and denominator with -b+√b^2-4ac/2a
#Result changes and its difference with the found quadratic solution before is -1.1641532182693481e-10
#The reason for that in the multiplication operation the fraction changes and it reflects the changes with a difference as denoted above


"""
## Q5 - Quadratic Solution Part(c)
"""

def QuadraticEquationSolver():
    a = int(input("Please enter the 'a' value in the quadratic equation: "))
    b = int(input("Please enter the 'b' value in the quadratic equation: "))
    c = int(input("Please enter the 'c' value in the quadratic equation: "))
    
    if a == 0:
        print("This equation is not an quadratic equation!!!")
    else:
        discriminant = ((b**2) - (4*a*c)) 
      
        # checking condition for discriminant
        if discriminant > 0: 
            print("There are 2 real different roots") 
            print((-b + math.sqrt(abs(discriminant)))/(2 * a)) 
            print((-b - math.sqrt(abs(discriminant)))/(2 * a)) 

        elif discriminant == 0: 
            print("There are 2 real roots but they are equal") 
            print(-b / (2 * a)) 

        # when discriminant is less than 0
        else:
            print("There are 2 complex different roots") 
            print(- b / (2 * a), " +", math.sqrt(abs(discriminant)),"i") 
            print(- b / (2 * a), " -", math.sqrt(abs(discriminant)),"i") 

QuadraticEquationSolver()

"""
## Q6 - The Derivative Part(a)
"""

def f(x):
    return x*(x-1)

def derivative(function, value, sigma):
    top_part = function(value+sigma) - function(value)
    bottom_part = sigma
    slope = top_part/bottom_part
    
    return float("%2.25f" % slope)

Derivative = derivative(f,1,10**-2)
print(Derivative)
#The reason for the difference between the analytically calculated derivative and at point 10^-2 is that
#In the derivative calculation with the limit definition we observe that whenever we are getting close to zero
#the resultatn function gives us 0/0
#Hence we apply the L'Opital rule which means we are assuming that the tangent line that we draw will be with zero angle
#But we also understood that whenever we are getting sigma close to zero result of the definition getting close to 1


"""
## Q6 - The Derivative Part(b)

"""

SigmaMinusFour = derivative(f,1,10**-4)
SigmaMinusSix = derivative(f,1,10**-6)
SigmaMinusEight = derivative(f,1,10**-8)
SigmaMinusTen = derivative(f,1,10**-10)
SigmaMinusTwelve = derivative(f,1,10**-12)
SigmaMinusFourteen = derivative(f,1,10**-14)
print("Derivative with sigma 10 over -4 is: " + str(SigmaMinusFour))
print("Derivative with sigma 10 over -6 is: " + str(SigmaMinusSix))
print("Derivative with sigma 10 over -8 is: " + str(SigmaMinusEight))
print("Derivative with sigma 10 over -10 is: " + str(SigmaMinusTen))
print("Derivative with sigma 10 over -12 is: " + str(SigmaMinusTwelve))
print("Derivative with sigma 10 over -14 is: " + str(SigmaMinusFourteen))

#We observe that when we continously decreasing the value of sigma (which getting close to 0) result of the function
#also gives us the value close to 1
#We may conclude that even the function output is getting far or close to the 1 (as in the case of true output)
#we are still converging to 1 from left side or right side
#which also indicates that when we are really close to zero derivative will approximate to 1

"""
## Q6 - Integral of a Semicircle Part(a)

"""

import math 

def RiemannSeriesIntegral(N):
    delta_x = 2/N
    start = -1
    end = 1
    def f(x):
        return math.sqrt(1 - (x**2))

    sum_of_areas = 0
    counter = -1
    while counter < 1:
        area = f(counter)*delta_x
        sum_of_areas += area
        counter += delta_x

    return sum_of_areas
s = RiemannSeriesIntegral(100)
print(s)

#The result is slightly different than the result that we obtained from the regular integral
#Even the result with Riemann Integral is close to the real value there is difference between them
#The reason for this we are dividing the area into rectangles an we are approximating the underneath area not completely correct
#There are some areas that are missing which is not taking into consideration in the Riemann Integral calculation
#That is why we obtained the integral with Riemann Integrall approach little bit smaller than the actual calculation

"""
## Q6 - Integral of a Semicircle Part(b)
"""

for N in range(100,150):
    print("For N is equal to: " + str(N))
    %time RiemannSeriesIntegral(N)
    print("-----------------------------")
#When we increas N we know that we are decreasing the width which results in that there will more rectangles
#that will cover the are, in other words there will more rectangles where each of them covers better the desired area
#Even though increasing the N value will result in an increase in time complexity for the calculation
#It is a nice drawback to obtain a more accurate calculation

#Hence, it can be observed that increasing the calculation up to 1 minute will result in a more precise calculation
#of the area that the integral covers even though it takes more time than the previous approaches