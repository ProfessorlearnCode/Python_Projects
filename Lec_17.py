# Lecture about Loops specifically For loops (Part 1)
##########################################################################################
# Looping is used to repeat a set of statements for a specific number of time or until a given condition is fulfilled
# Loops are classfied in python as For and While loop

name = "Professor"                                      # 'Name' Variable with string data
for i in name:                                          # For loop with initialized variable 'i' which is being iterated in 'Name'
    print(i)                
print(end="\n-------------------------\n")

color = ["Red","Orange", "Blue", "Yellow", "Green"]     # It comprises of a 'list', multiple strings in one variable
for color in color:                                     # For loop with initialized variable 'color' which is being iterated in 'color'
    print(color)            
    for i in color:                                     # Nested loop structure
        print(i)
print(end="\n-------------------------\n")

# Range syntax will be (Start(X), Stop(Y), Step(Z))
# Start --> The starting index of the loop, if not given python automatically assumes '0'
# Stop --> The Stoping index of the loop, it is compulsory to provide
# Step --> It jumps over the provided intervals like when 2 is given it jumps '2 values' in each iteration

for k in range(10):                                     # Range is used as n-1
    print(k)
print(end="\n-------------------------\n")

for k1 in range(10):              
    print(k1+1)
print(end="\n-------------------------\n")   
 
for startstop in range(1,9):                            # X will be "start" marker and Y will be "stop" marker but Y-1
    print(startstop)
print(end="\n-------------------------\n")

for startstopstep in range(1,11,2):
    print(startstopstep)
print(end="\n-------------------------\n")    
    
# Quick Quiz
# What is the functioning of the "Step Parameter" in for loop?



