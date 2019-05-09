a=1
b=2
user_name = "Muyanme"
def addition(*args):
    print(sum(args))
def Subtraction (a,b):
    print(abs(a-b))
def Multiplication(a,b):
    print(a*b)
def Division(a,b):
    if b!=0:
        print(a/b)
    else:
        print("Denominator should be abs non zero value!")
        
print(__name__)
        
if __name__ == "__main__":
    addition(1,2,3)
    Subtraction(1,2)
    Multiplication(2,3)
    Division(4,5)