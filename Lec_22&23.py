# Lecture about lists and introduction to List Comprehension
# Lecture about List methods
###########################################################################
# List is a ordered collection of data items with preferably same datatypes but different datatypes can be bundled
# Lists are seperated by commas (,) and enclosed in []
# We can add data items in lists but can't add in Tuples

Marks = ["Ali", 19, True]
print(Marks[0])                                            # We can also use indexing
print(Marks[1])                                            # We can also use indexing
print(Marks[2])                                            # We can also use indexing
print(Marks[-1])                                           # For -ve index, Subtract the index from total length


List = [0, 1, 2]
print(List)
print(type(List))
print(List[0])                                             # We can also use indexing
print(List[1])                                             # We can also use indexing


# If we want to determine a specific value in a list we can use Conditional statment

listofnumbers=[0, 1, 2, 3, 4, 5, 6, "Professor", 8, '-']
if "Professor" in listofnumbers:                           # Use "" Wisely as "6" & 6 are different, Same applies for strings
    print("Yes")
else:
    print("No")
    
# If we can use different techiques to see the entries and even use list slicing and stepping (Same as string slicing and stepping)

print(listofnumbers)
print(listofnumbers[:])
print(listofnumbers[1:5])
print(listofnumbers[1:8:2])

# List Comprehension

lst=[i for i in range(4)]
print(lst)

lst=[i for i in range(10) if i%2==0]                        # Prints Even Numbers with in a list 
print(lst)


# List methods --> Used to modify the entries of the list 

l = [1, 2, 3, 4, 5, 6 , "Professor"]
l.append("New Entry")                                       # Adds a new entry at the end of the list
print(l)

l1 = [2, 5, 1, 6, 4, 7 ]
l1.sort()                                                   # Sorts the entries of the list in ascending order
print(l1)

l2 = [2, 5, 1, 6, 4, 7 ]
l2.reverse()                                                # Reverse the entries of the list as it it is
print(l2)

l3 = [2, 5, 1, 6, 4, 7 ]
print(l3.index(4))                                          # Returns the index of the 1st occurence of the specified list item

l4 = [2, 5, 1, 6, 4, 7, 4, 6, 2, 1 ]
print(l4.count(4))                                          # Returns the number of occurences of the specified list item



# In case of indexing, we have to be careful of the following case
# We have to use the "copy method" when assigning the lists from variables as normally it will create a refrence to the original list and 
# any changes done in newlist will result in the original list

originallist = [1,2,3,4,5,6,7,8,9,10]                       # We made a base list 
#newlist = originallist                                     # Then we 'Assigned' the list to another variable
newlist = originallist.copy()                               # Then we 'Assigned' the list to another variable
newlist[0] = 999                                            # Changed the data items using indexing
print(originallist)                                         # The change is showed in the base list 
print(newlist)                                              # By using "Copy()", only newlist is affected with changes

print(originallist.insert(1, 200))                          # Inserts a specified data item at a specified index (index, Data)


# You can concatinate or extend two lists 

firstlist= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secondlist = [000, 111, 222, 333, 444, 555]
firstlist.extend(secondlist)                                # Extends the 1st list with the data of 2nd list
print(firstlist)
k = firstlist + secondlist                                  # Concatination of 2 strings
print(k)

































