# ECHO is on.
print("try Except Else")
try:
    print("try")
    print(10/0)
except:
    print("Except")
else:
    print("else") # If no error then else block will exectute.
                  # If any error except block will execute.
print("try Except finally")
try:
    print("try")
    print(10/0)
except:
    print("Except")
finally:
    print("finally")