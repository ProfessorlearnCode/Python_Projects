# Lecture about tuples and basic tuple methods
####################################################################
# Tuples are ordered collection of data items which are immutable (unchangable)

tup = (1, 2)
print(type(tup), tup)

tup1 = (1,)                                                                   # This will identify as an int so use a comma
print(type(tup1), tup1)

# tupwrite = (1, 2, 3, 4)
# tupwrite[0] = 999                                                           # 'tuple' object does not support item assignment                              
# print(type(tupwrite)) 

# Data is read from tuple using indexing

tupread = (1, 2, 3, 4)                            
print(tupread[0], tupread)                                                    # We cannot write data into the tuple however We can read data from tuple
print(tupread[1], tupread)                                                    # We cannot write data into the tuple however We can read data from tuple
print(tupread[2], tupread)                                                    # We cannot write data into the tuple however We can read data from tuple
print(tupread[-2], tupread)                                                   # We cannot write data into the tuple however We can read data from tuple

# Tuples can also be sliced using same concepts, However the sliced tuple is a complete different tuple

Tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(Tuple[:5])
print(Tuple[:])
print(Tuple[3:4])
print(Tuple[-4])


# tuple methods --> Used to modify the entries of the tuple 

T1 = [2, 5, 1, 6, 4, 7 ]
T1.sort()                                                                       # Sorts the entries of the tuple in ascending order
print(T1, end="\n-----------------------\n")

T2 = [2, 5, 1, 6, 4, 7 ]
T2.reverse()                                                                    # Reverse the entries of the Tuple as it it is
print(T2, end="\n-----------------------\n")

T3 = [2, 5, 1, 6, 4, 7 ]
print(T3.index(4), end="\n-----------------------\n")                           # Returns the index of the 1st occurence of the specified Tuple item

T4 = [2, 5, 1, 6, 4, 7, 4, 6, 2, 1 ]
print(T4.count(4), end="\n-----------------------\n")                           # Returns the number of occurences of the specified Tuple item

# # You can concatinate or extend two tuples 

firsttuple= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
secondtuple = (000, 111, 222, 333, 444, 555)
print(firsttuple)
k = firsttuple + secondtuple                                                      # Concatination of 2 Tuples
print(k)




















