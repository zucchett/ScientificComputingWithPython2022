def my_decorator(f): 
    def log_f_as_called():
        print(f'{f} was called.')
        f()
    return log_f_as_called

@my_decorator
def hello():
    print('Hello World!')
    
hello()