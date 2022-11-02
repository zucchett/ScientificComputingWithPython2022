def underflow(x:int = 1):
    while True: 
        x = x / 2
        print(x)

def overflow(x:int = 1):
    while True:
        x= x*2
        print(x)

def main():
    underflow()
    overflow()

main()

