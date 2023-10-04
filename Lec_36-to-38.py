# Lecture about Error/Exceptional handling and raising Custom Errors
#####################################################
'''
Sometime we may fall into an error, We can use various methods and techniques to anticipate and deal with
those Errors/Exceptions.

'''

# The program demands an integer
# In case of an input other than int, the program will show an error so for this we use try-except


try:
    a = int(input("Enter number: "))        
    print(f"The table for {a}")
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")
           
except (ValueError,IndexError):
    print("Invalid Value!")
    
###################################################
    
try:
    user_input = int(input("Enter integer input: "))
except:
    print("Invalid input")    


####################################################
'''
We sometimes need to give a proper closure to the exception statements 
So we use 'Finally', to indicate that the code is properly handled
it is always exected after the exception handling

We use 'Finally' when we are dealing with a function 
Finally returns its content irrespective of the returning value and ending of the function
In short, Used for clean up

'''

try:
    user = int(input("Enter Value"))
except:
    print("invalid")
    
print("I am always executed")

#####################################################################

def function():
    try:
        LIST = [1, 2, 3 ,4, ]
        user_index = int(input("Enter an index: "))
        print(f"The value at index[{user_index}] --> {LIST[user_index]}")
        return 1
    except IndexError:
        print("Invalid index")
        return 0
    finally:
        print("This is 'finalised'")
        
print(function())
    
###################################################################

'''
When we are dealing with python, we can raise custom errors to stop the execution of the program
by using 'raise' we can raise custom errors.

'''

number_input = int(input("Enter value(5-9): "))

if number_input > 9 or number_input < 5: 
    raise ValueError("The value should be between 5-9")

# We can create/define our own custom Error based on classes and inheritence


# Quick Quiz
# Raise an Error except when the user enters "quit" 

Q = input("Enter 'quit': ")

if not Q == "quit":
    raise ValueError("You have to enter 'quit'")
    


