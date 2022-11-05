def hello(func):
   def wrapper(w):
       print("Hello World")
       func(w)  
   return wrapper
@hello
def square(w):
   print(w*w)
square(56)

