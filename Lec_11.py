# Lecture about Strings and implementation of Multi-line string, Also the implementation of indexing in strings 
################################################################################################################

name = "Farzam"                                 # We can use single qoutes
Sirname = 'Asad'                                # We can use double qoutes
friend = "Professor"                            # It doesn't matter which one you choose
print("Hello " + name + Sirname + friend)       # Used '+' to concatenate different parameters of the string

# We can use Different combinations of Qoutation
hobby = 'He said, "he wants to learn to code"'
print(hobby)

# Using '''/''' for multiline outputs  
print("\nConeversation between 2 friend",end="\n")
Multiline_Statements = '''Ahmad: Hello there
Umar: Hello!
Ahmad: What are are you doing?
Umar: Nothing really!!'''
print(Multiline_Statements)


# String is like an array of characters that we can access using indexing
# We can print the characters one by one or use a loop
print("\nUsing indexing to print out the character of a string")
print(name[0])                                  # Prints F
print(name[1])                                  # Prints A
print(name[2])                                  # Prints R
print(name[3])                                  # Prints Z
print(name[4])                                  # Prints A
print(name[5])                                  # Prints M
#print(name[6])                                 # Shows an Error because 6th index is empty 


# Using loops to print the characters of the string
# Details about loops is discussed in lecture 17
print("\nUsing looped indexing to print out the character of a string", end="\n")
for character in name:
    print (character)