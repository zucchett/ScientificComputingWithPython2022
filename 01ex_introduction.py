from math import sqrt as sqrt

##########
# PART 1 #
##########
def part_one():
    results = []

    # Iterate over 1-100
    for i in range(1,101):
        if i % 15 == 0:
            print("HelloWorld")
            results.append("HelloWorld")
        elif i % 3 == 0:
            print("Hello")
            results.append("Hello")
        elif i % 5 == 0:
            print("World")
            results.append("World")
        else:
            print(i)
            results.append(str(i))

    # Update the contents based on the requirements
    for index, each in enumerate(results):
        if "Hello" in each:
            results[index] = results[index].replace("Hello","Python")
        if "World" in each:
            results[index] = results[index].replace("World","Works")

    return(tuple(results))

print(part_one())

print("-------------------")
##########
# PART 2 #
##########
def part_two():
    x = input("Enter x: ")
    y = input("Enter y: ")
    x , y = y , x
    print("X is: {}, and y is: {}".format(x,y))

print(part_two())

print("-------------------")
##########
# PART 3 #
##########
def euclidian_distance( u , v):
    distance = sqrt( (u[1]-v[1])**2 + (u[0]-v[0])**2 )
    return distance

print(euclidian_distance((3,0),(0,4)))

print("-------------------")
##########
# PART 4 #
##########
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def character_counter( string ):
    # Create a distinct characters dictionary
    character_dict = {}
    # Eliminate capitalization differences
    for character in string.lower():
        # If haven't already added the character
        if character not in character_dict.keys():
            character_dict[character] = 1
        # If have already added the character
        else:
            character_dict[character] = character_dict[character] + 1
    return character_dict

result = character_counter(s1)
print("There are {} characters in the text".format(result))

print("-------------------")
############
# PART 5/A #
############
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def unique_numbers(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("There are {} unique numbers".format(len(unique_numbers)))
    print("Unique numbers are {}".format(unique_numbers))

unique_numbers(l)


print("-------------------")
############
# PART 5/B #
############

# We first use set method to eliminate the duplicates and then return them as a list 
unique_numbers = list(set(l))

print("Using data structures, there are {} unique numbers".format(len(unique_numbers)))
print("Unique numbers are {}".format(unique_numbers))

print("-------------------")
##########
# PART 6 #
##########
def type_converter():
    allowed_types = [int, float, str]
    result = None

    var1 = input("Enter an integer, float or string for variable 1: ")
    var2 = input("Enter an integer, float or string for variable 2: ")

    # We iterate over all the possible combinations of input / output types
    for first_type in allowed_types:
        for second_type in allowed_types:
            # If a conversion is possible return the solution
            try:
                result = sum([first_type(var1),second_type(var2)])
                break
            except:
                continue
        if result:
            break

    if result:
        print("Result is",result)
    else:
        print("You have entered incompatible types to add")

type_converter()

print("-------------------")
############
# PART 7/A #
############
list_of_cubes = []
for i in range(11):
   list_of_cubes.append(pow(i,3))
print(list_of_cubes) 

print("-------------------")
############
# PART 7/B #
############
list_of_cubes = [pow(i,3) for i in range(11)]
print(list_of_cubes)


print("-------------------")
##########
# PART 8 #
##########
a = [ (i,j) for i in range(3) for j in range(4) ]
print(a)


print("-------------------")
##########
# PART 9 #
##########
solutions = [ (a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if pow(a,2) + pow(b,2) == pow(c,2)]
print(solutions)


print("-------------------")
###########
# PART 10 #
###########
def normalizer( tup ):
    # Sum the squares of each element in the input tuple of varying length
    sqrt_sum = sqrt(sum( pow(each,2) for each in tup))
    # Normalize each element based on the squared sum
    normalized_vector = tuple([each/sqrt_sum for each in tup])
    return normalized_vector

normalizer((3,4,5))

print("-------------------")
###########
# PART 11 #
###########
def loopFibonacci(n):
    initial = [0,1]
    while len(initial) < n:
        initial.append( initial[-1] + initial[-2] )
    return initial

print(loopFibonacci(20))