# Lecture about Break and Continue Statements
###################################################################
# If we want to skip/stop an iteration of a loop then we use break and continue
# Break --> It is used to stop the execution of the iteration then, exits of the body of loop
# Continue --> It is used to stop the executtion of the iteration then, exits the current iteration

for b in range(21):
    if(b == 10):
        break                       # It exits the body of the loop
    print("2 x",b,"=",2*b)
    
print("Loop Excecuted", end="\n--------------------------------\n")



for c in range(21):
    if(c == 10):
        continue                   # It exits the current iteration of the loop, then continue to the next iteration
    print("2 x",c,"=",2*c)
    
print("Loop Excecuted", end="\n--------------------------------\n")    