#Lecture about Print function and its uses alongwith 2 parameters
#Lecture about the use of escape sequences
#Lecture about the comments
#############################################################################
# This is a comment 
# To Comment multiple lines ==> Ctrl + /

'''
This 
is
a
Multi-line
Comment
'''
# Use Ctrl + l to clear the terminal

print("Now we use escape sequences\nThis is how it is done")    # Use escape sequences like usual 

print("We also use escape Sequences for this \"Purpose\"")      # Use escape sequences like usual

print("We also use escape Sequences for this \'Purpose too\'")  # Use escape sequences like usual

# 'sep=' is used to separate each entity (separator parameter)
# 'end=' is used to specify what to print at the end of the line (Like endl parameter)

print(327, 8891054, sep="-", end="\n")
print("This line is after the end=\" \"")      
print("---------------------------------------------------")

# We use Sep to separate the entites of the print statement with the 'end line escape sequence'
print("Name","Farzam",sep="\n") 