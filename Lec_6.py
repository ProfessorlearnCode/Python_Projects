# Lecture about initialization of Variables
########################################################################

a=1.111111                  # No quotations for Numeric Data
print(a)
a_complex= complex(1, 2)    # Use "complex()" for Complex data eg. (1+2j)
print(a_complex)
b="Professor"               # Double qoutation for String Data
print(b)
c='A'                       # Single qoutation for Character Data
print(c)
d=True                      # No quotations for bool Data
print(d)

# If we want to determine the datatype of a variable use type(Var_name)

print("The type of a is", type(a))
print("The type of b is", type(b)) 
print("The types of c is", type(c))                # Characters are a subset of String 
print("The type of d is", type(d))