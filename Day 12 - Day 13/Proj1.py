
a=6
b=8
mystring="Python is Awsome!"


def evenodd(x):
    if x%2==0:
        print("{} is even".format(x))
    else:
        print("ODD")

def printNaturalNumbers(till):
    print(list(range(0,till+1)))

if __name__=='__main__':
	evenodd(3)


