# Lecture about short hand if-else
##########################################################
# If-else are conditional statements which are used to check whether a situation is according a specific condition
# Sometimes shorthanding is blessing, sometimes it is a curse
# Always write a code that can be easily maintained

a = 3000
b = 300
print("A") if a > b else print("=") if a == b else print("B")               # We can cram the entire conditional in one statement following a syntax


c = print(9) if a>b else 0                                                  # We can also assign it to another variable, However it is not very 'suitable'
print(c)