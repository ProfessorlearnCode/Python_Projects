# Lecture about function Arguements and its types (Part 2)
###############################################################################
# Function arguments are the parameters/variables used for the execution of user-defined function
# There are 4 types
# --> Default Argurments
# --> Keyword Arguments
# --> Variable length Arguments
# --> Required Arguments

# Default Arguments --> used to assume a default when actual parameter is not provided

def avg(x = 0, y = 0):                          
    print(f"Average is {(x+y) / 2}")

print("The average with default arguments ")   
avg()                                                       # Here Default Arguments will be assumed
print("The average with provided arguments ")   
avg(1, 5)                                                   # If parameters are provided then the default arguments will be overwritten

def nameinput(fname = "Farzam", mname = "", lname = "Asad"):
    print("Hello:",fname,mname,lname)
nameinput()

# Keyword Arguments --> used to define the actual parameters with their names so order of the parameters doesnot matter

def add(x = 1, y = 2):
    print("Sum is :",x + y)
add(y = 4, x = 1)                                           # We have specified the variable used for this function

# Required Arguments --> In case we don't use a default argument for a parameter, it is required for us to insert an argument in that variable

def subtract(x, y = 2):
    print("Subtraction is :",x - y)
subtract(x = 1 , y = 1)                                     # It is necessary for us to provide the argument for x parameter

# Variable length Argument 

def average(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    print("Average is ",sum/len(numbers))
average(1,2)

# If we want a function to "return" a value then we store that value in another variable then,

def multiplication(x, y):
    multiply = 1
    multiply = x * y
    return multiply                                         # Function returns a value 

m = multiplication(1,2)                                     # The function returned value is stored in a different Variable
print(f"The ans: {m}")                                                 