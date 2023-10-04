# Lecture about Typecasting and its types
#######################################################################################################
# Typecasting is the conversion of one datatype into another data type. Also known as "Type Conversion"

a="1"                                   # This is a string
b="2"                                   # This is a string
# a = "Farzam" | b = "2"    --> Hence this case is invalid as string
print(int (a) + int (b))


# Explicit Typecasting --> The dev is purposely doing the conversion like int(), float(), hex(), oct(), str(), etc.
print("\nExplicit Typecasting", sep="-")
string = "15"                           # This is a string
number = 15                             # This is integer
string_number = int(string)             # Conversion of "string"(str) into int explicitly
sum = number + string_number            # Using both numbers and string_numbers
print("The sum of both the numbers is :", sum)

# Implicit Typecasting --> Each datatype have a specific precedence/order while using an operator, So python interpreter 
# does the conversions.

print("\nImplicit Typecasting", sep="-")
c = 1.9                                 # This is a floating 
d = 9                                   # This is an integer
print(c + d)                            # Compiler implicitly converts the int => float 
  