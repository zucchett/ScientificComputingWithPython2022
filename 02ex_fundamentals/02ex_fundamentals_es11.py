import math
class polygon:

    x=()
    def __init__ (self,slength):
        if len(slength)<3:
            print("Side count must be 3 or more")
        else:
            self.x = slength
        
    def perimeter(self):
        a = sum(self.x)
        print ("The primeter is:",a)
    def getOrderedSides(self, b):
        s_tuple = sorted(self.x)
        if b == True:
            print(s_tuple)
            return s_tuple
        else:
            c=[]
            c = s_tuple
            c.reverse()
            print(c)
            r_tuples =()
            r_tuples = c
            return r_tuples
            
class Rectangle(polygon):

    def __init__(self,s):
        if len(s)==4 and s[0]==s[1] == s[2]==s[3]:
            print("Its an square")
        elif len(s)==4 and s[0]==s[2] and s[1]==s[3]:
            self.x=s
        elif len(s)==4 and s[0]==s[1] and s[2]==s[3]:
            self.x=s
        elif len(s)==4 and s[0]==s[3] and s[1]==s[2]:
            self.x=s
        else:
            print("Its not a rectangle")

    def area(self):
        length= max(self.x)
        width=min(self.x)
        a = (length*width)/2
        print("The area is:",a)
        return

r = Rectangle((3,20,3,20))
r.area()
r.perimeter()
