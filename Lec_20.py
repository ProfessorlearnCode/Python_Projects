# Lecture about Functions and introduction to User-defined functions (Part 1)
######################################################################
# Sometimes we develop our own function logic and use it in our code 
# A funtion is a block of code which perform a specific task when it is called
# There are 2 type of functions 
# --> User-defined  
# --> Built-in Function


a = 2
b = 2
gmean = (a * b) / (a + b)
print(f"Geometric Mean  = {gmean}")


# This function calculates mean as parameters are used it is said to be a parametized
# The parameters for the function during initialization called as Formal Parameters
def calculatemean(a, b):                       
    mean = (a * b) / (a + b)
    print(f"Geomatric mean function = {mean}")


# The parameters for the function during Calling called as Actual Parameters
first = 3
second = 4
calculatemean(first, second)                    # The "calculatemean" is called and used wrt to the given parameters                                


def isgreater(x, y):
    if x > y:
        print("1st number is greater than 2nd number")
    elif x == y:
        print("1st number and 2nd number is equal")
    else:
        print("2nd number is greater than 1st number")

def islesser(x, y):
    pass                                        # 'pass' tells the interpreter that we will use this function in the future
        
        
c = int(input("Enter 1st number: "))
d = int(input("Enter 2nd number: ")) 
isgreater(c, d)
calculatemean(c, d)


     