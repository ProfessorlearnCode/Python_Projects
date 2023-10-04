# Lecture about Local and global variables
#########################################################################
# A variable is a memory location
# When create a program there are to 2 variables 
# --> Local Variable (variables used with the scope of a specific function)
# --> Global Variable


x = 4 
print(f"This is Global Variable: {x}")

def local():
    y = 5
    print(f"This is local Variable: {y}")
    

# However

def init_global():
    global z    # We can also change/use the outer global variable within a function
    z = 5
    print("This is a global variable used locally: {z}")
    
    
local()
print(x)
# print(y)        # As y is local variable in local() so it cannot be used globally
print(z)

