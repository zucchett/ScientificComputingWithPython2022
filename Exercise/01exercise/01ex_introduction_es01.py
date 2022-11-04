# Excersize 1-a:
a_list = [1]
for i in range(2,101):
    if i % 15 == 0:
        a_list.append("HelloWorld")
    elif i % 3 == 0:
        a_list.append("Hello")
    elif i % 5 == 0:
        a_list.append("World")
    else:
        a_list.append(i)
#print(a_list)

# Excersize 1-b: 
t1_tuple = tuple(a_list)                     #Convert list to tuple
#print(t1_tuple)
#b_tuple[3] = 'Python'
#print(b_tuple)

#As the Tuple cannot be changed, I put the list to the string variable and replace the "Hello" ->"Python & "World" ->"Works" then return it to a tuple variable
s = ''.join(str(i)+' ' for i in a_list)     #Convert list to string
s= s.replace('Hello','Python')              #Replace some characters in the string
s= s.replace('World','Works')
#print(s)
b_list = s.split(' ')                       #Split the string and return it to the list
b_list = b_list[:-1]                        #Remove the last member of the list(here it was an extra space)
#print(b_list)
t2_tuple = tuple(b_list)
print(t2_tuple)