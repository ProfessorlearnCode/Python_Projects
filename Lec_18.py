# Lecture about loops specifically While loop (Part 2)
#####################################################################################
# While loops execute a set of statements when a specific condition is fulfilled
# The loop is executed until the condition remains 'True', then it exits the loop body

for i in range(3):
    print (i)
print("Loop Executed\n------------------------------\n")
    
i= 0
while (i <= 3):                               # The i is less than 3, so it is a incrementing loop
    print(i)                                  
    i= i + 1                                  # Incrementation
print("Loop Executed\n------------------------------\n")

while (i < 100):
    i = int(input("Enter a number:"))
    print(i)
print("Loop Executed\n------------------------------\n")

count = 5                                       # The count variable is used
while (count > 0):                              # The count is greater than 5, so it is a decrementing loop
    print (count)
    count = count - 1                           # Decrmentation
else:
    print("Loop Executed\n------------------------------\n")


# Do-while loop is not found in Python, But the emulation can be done using Break/Continue functions from lecture 19
# Do-while loop is similar to While, but it executes the body at least once 

i=0
while True:                                       # Using an infinite loop as it will be iterated irrespectively
    print(i)
    i=i+1
    if(i%100 == 0):
        break
print("Loop Executed\n------------------------------\n")
    
while True:
    number = int(input("Enter a number"))
    print(number)
    if not number > 0:
        break
print("Loop Executed\n------------------------------\n")