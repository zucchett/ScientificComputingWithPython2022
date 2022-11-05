def swap_function(x, y): 
    x = x + y
    y = x - y
    x = x - y
    print("After swaping, x: %.1f, y: %.1f" % (x, y))    
swap_function(-5.6, 10.3)