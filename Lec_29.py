# Lecture about Docstrings 
#############################################
# Docstrings are not ignored unless comments
# This is a special kind of string
# Docstrings are on the "right below the name of the function"
# Docstring are used to document the function the programs

def square(n):
    '''Takes in a number n and it returns the square of n!''' # This is a doc string
    print(n*n)
    
square(5)
print(square.__doc__)