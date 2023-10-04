# Lecture about Matching case statements (Switch Statements)
##################################################################################################
# Match case statements consists of 2 or more conditions on which the instruction falls in one of the condition
# In C++, We use "Break" to end the body of the switch but python is intelligent and it only executes the body of the matching case

x = int(input("Enter value of X: "))

match x:                                            # The Variable 'x' will be used for matching
        case 0:                                         # Case 0 matching                     
            print("X is zero\n")
        
        case 1:                                         # Case 1 matching
            print("X is one\n")

        case 2:                                         # Case 2 matching
            print("X is two\n")

        case _ if(x > 2):                               # We use default case syntax for implementing conditional statements in case statements
            print("The X is greater than 2")
        
        case _ if(x < 0):                               # If statements can be used as a case statemnt
            print("The X is less than 0")
        
        case _:                                         # Default Case if none match the above cases
            print("Invalid Input")