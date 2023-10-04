# Lecture about Tuple methods
#############################################################
# As we know that tuples are a form of list which are immutable 


tuple1 = (0,2,3,4,5,6,7,8,7,8)
result = tuple1.count(7)                    # Count() is used to count the number of specifed data
print("7 repeats at ",result)


tuple1 = (0,2,3,4,5,6,7,8,7,8)
result1 = tuple1.index(0)                    # index() is used to return the first index of the specified data
result2 = tuple1.index(5,2,4)                # If we want to find the occurance in a specific length then use slicing
print("0 repeats at ",result1)
