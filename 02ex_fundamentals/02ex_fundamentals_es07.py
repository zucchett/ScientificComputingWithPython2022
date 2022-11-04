def hello(f): 
    def log_f_as_called():
        print(f'{f} was called.')
        f()
    return log_f_as_called

@hello
def hello():
    print('Hello World!')
    
hello()