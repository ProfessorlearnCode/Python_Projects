# Solution to a problem which greets the user to their local time
###########################################################################

# Importing an external library named "time" more in the future tutorials

import time
print("The number of seconds for epoch",time.time(),end='\n--------------------------------------\n')       # Time passed in seconds from the epoch (1970)
print(time.ctime(),end='\n-------------------------------------\n')                                         # Time in regular format from the epoch to today 

print(time.localtime(),end='\n---------------------------------\n')                                         # Shows local time with multiple parameters like Yr, mn, day, hr, min, sec, wkday, yrday 
help (time.ctime)  

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