# Lecture about User input and implementing Type-casting 
#################################################################################

name = input("Enter your name: ")
print("Hello",name)

print("Enter 2 numbers to be added",end="\n")
x = input("1st number: ")
y = input ("2nd number: ")
print (x + y,"(Incorrect)",end="\n\n") 

# As it takes the value a String so it Concatenates the inputs instead of performing operation                           
# Python doesn't recognize the datatype of the input value, It always identifies the value as String, so we use type-casting
# to convert the datatype into our desirable type according to our condition


print("Enter 2 numbers to be added",end="\n")
x = input("1st number: ")
y = input ("2nd number: ")
print (int (x) + int (y),"(Correct)",end="\n")