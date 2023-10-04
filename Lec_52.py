# Lecture about lambda functions
########################################################
# Lambda functions are the types of functions which are anonymous functions without a name
# Lambda can be used when you are trying to compress the code into one liner
# They are used when functions are to be used as arguments

def double1(x):
    return x*2

print(double1(2))

double2 = lambda x: x*2
print("This is using a lambda function --> double2:",double2(2),end ="\n")

cube = lambda x: x*x*x
print("This is done using Lambda function --> Cube:",cube(2),end ="\n")

average = lambda x,y: (x+y)/2
print("This is also done using lambda function --> avg:",average(2,2),end ="\n")