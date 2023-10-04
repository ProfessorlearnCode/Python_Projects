# Lecture about Decision and Conditional Statements and 
# Excercise # 2 : A small intro introduction about {Time module}
#################################################################################################
# Conditional Statements are used to check the validity of an input or logic wrt to a specified condition
# Conditional operators: <>, <=, >=, !=, ==

a=int(input("Enter your age: "))
print("Is the age equal to 18: ",a==18)
print("Is the age Smaller than 18: ",a<=18)
print("Is the age Greater than 18: ",a>=18)
print("Is the age not equal to 18: ",a!=18)


if(a>18):
    print("You can Drive")                                                                      # The syntax includes indentations
else:
    print("You cannot Drive")
print("This will be printed",end='\n---------------------------------\n')                       # This line will be printed as it is outside the body of the condition 

applePrice = 190
budget = 200
print("The price of apple is", applePrice,"\nThe Budget is", budget)
if(applePrice<=200):
    print("Add to cart")
    print("Your remaining Balance is",int(budget)-int(applePrice),end='\n---------------------------------\n')
else:
    print("Apples are expensive from the budget",end='\n---------------------------------\n')
    
    
# Program to determine whether the input is +ve/-ve using elf

print("Positive/Negative number checker\n")  
num = int(input("Enter the value of Num: "))
if (num < 0):
    print("Number is negative")
elif (num == 0):
    print("The number is 0")
else:
    print("Number is positive",end='\n---------------------------------\n')


# Program to determine the sign of input number   
 
number = int(input("Enter a number: "))
if(number > 0):
    print("The number is Greater than 0",end='\n---------------------------------\n')
    if (number <= 10):
        print("The number is between 0-10",end='\n---------------------------------\n')
    elif(number > 10 and number <= 20):
        print("The number is between 10-20",end='\n---------------------------------\n')
elif(number < 0):
    print("The number is smaller than 0",end='\n---------------------------------\n')
    if(number >= -10):
        print("The number is Smaller or equal to -10",end='\n---------------------------------\n')
    elif(number < -10 and number <= -20):
        print("The number is between -10 and -20",end='\n---------------------------------\n')
else:
    print("The number is zero",end='\n---------------------------------\n')  
    

# Importing an external library named "time" more in the future tutorials

import time
print("The number of seconds for epoch",time.time(),end='\n--------------------------------------\n')       # Time passed in seconds from the epoch (1970)
print(time.ctime(),end='\n-------------------------------------\n')                                         # Time in regular format from the epoch to today 

print(time.localtime(),end='\n---------------------------------\n')                                         # Shows local time with multiple parameters like Yr, mn, day, hr, min, sec, wkday, yrday 
help (time.ctime)                                                                                           # Shows "Help" for specific instrution


# Program to determine the local time and greet you accordingly

hours= int(time.strftime("%H"))                                             
Minutes = int(time.strftime("%M"))
if (hours <= 12):
    print("Good Morning Professor\nIt is currently",hours,":",Minutes,"Am")
elif(hours <= 18 ):
    print("Good Evening Professor\nIt is currently",hours,":",Minutes,"Pm")
elif(hours <= 24 ):
    print("Good Night Professor\nIt is currently",hours,":",Minutes,"Pm")
else:
    print("You dead")