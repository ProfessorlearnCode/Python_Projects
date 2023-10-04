# Lecture about a For-loop else statement
#####################################################
# 'else' is used with if for conditional use
# It can also be used with loops,
# The else body will be executed after the body of the loop


for i in range(5):
    print(i)
    
else:
    print("Sorry no i")
print('-----------------------------')
    
for i in range(10):
    print(i)
    if i == 4:
        break    
else:                           # The content of the 'else' will not be executed because the while is affliated with for-loop and if the
    print("Sorry no i")         # loop is exited the the else statement is ignored 
    
print("This is printed after Loop")
    