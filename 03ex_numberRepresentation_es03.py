def underflow(y:int = 1):
    while True: 
        y = y / 2
        print(y)

def overflow(y:int = 1):
    while True:
        y= y*2
        print(y)

def main():
    underflow()
    overflow()

main()

