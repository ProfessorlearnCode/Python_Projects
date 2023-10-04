# Lecture about the difference between 'is' and '=='
#####################################################
# Both are comparison operators
# is compares the location of the values in the memory
# == compares the values

a = 4
b = '4'

print(a == b)   # Returns False as the datatypes are different
print(a is b)   # Returns True as the location and memory location is different

l1 = [0,1,2]
l2 = [0,1,2]
print(l1 is l2)
print(l1 == l2)

value1 = 0      # Python uses the same memory locations as the values are same
value2 = 0      # Python uses the same memory locations as the values are same
print(value1 is value2)
print(value1 == value2)