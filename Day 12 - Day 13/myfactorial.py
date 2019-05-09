def fact(n):
    return 1 if n == 1 else n * fact(n-1)

print("Value inside __name__: ", __name__)

if __name__=="__main__":
    print(fact(5))