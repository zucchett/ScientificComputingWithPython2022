import sys

def main(argv):
    try:
        x = int(argv[1])
        y = int(argv[2])
        print (x+y)
        return x+y
    except ValueError:
        try:
            x = float(argv[1])
            y = float(argv[2])
            print (x+y)
            return x+y
        except ValueError:
            print("Please enter a number")
            return 0

if __name__ == "__main__":
    # print(len(sys.argv))
    main(sys.argv)