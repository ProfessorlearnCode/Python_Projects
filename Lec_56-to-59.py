# Lecture about Introduction about Object Oriented Programming, Constructors and Decorators
###############################################################
# There are 2 types of programming
# --> Functional / Procedural Programming
# --> Object Oriented Programming

'''
Example of Functional Programming;

def hello():
    print(hello)

hello()

'''

'''
In OOP, 
Class is a blueprint while,
objects are the entities that use that blueprint in order to perform a function
Classes provides base that can have various attributes and methods
We can use those attributes and methods through instances (objects).

--> OOP include inheritence, which revolves around pre-existing classes
and we can inherit different methods/ attributes those other classes
and extend a functionality of a new class with it's own attributes and 
methods.

'''
# self is a parameter which is a reference to the current instance of a class
# The self parameter is a reference to current instance of the class. 
# It is used to access the variables that belongs to the class.

class Person:
    name = 'Professor'
    occupation = 'Software Developer'
    networth = 10000
    def info(self):
        print(f"{self.name} is {self.occupation}")
       
a = Person()
a.name = "Nouman"
a.occupation = "Web developer"
a.info()

b = Person()
b.name = "Amna"
b.occupation = "Accountant"
b.info()

'''
Constructors is a special type of method used to create and initialize
the instance (object) of the class
constructor used the same name of class, it is invoked whenever an instance is created
Types of constructors;
--> Parameterized Constructor
--> Default constructor

'''

class Personn:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
    # def __init__(self):
    #     print("This is a default constructors")
        
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
person1 = Personn("Professor", "developer")          # Person() is a constructor used the same name of class, it is invoked whenever an instance is created
person2 = Personn("Filza", "Manager")                # Person() is a constructor used the same name of class, it is invoked whenever an instance is created

# person3 = Person()                                # It expects 2 arguments as self is ignored (name, occupation)

person1.info()
person2.info()


'''
Decorators is used modify the behaviour of methods, 
to extend the functionality of an existing function

'''

# We want to greet the user and thank the user at the end of each function
# Suppose we have 100+ function we can't afford to change all the functions 1 by 1
# It returns a 'Decorated Function'

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx()


@greet                          # 1st method to use decorator
def hello():
    print("Hello There!")
    
# greet(hello())                # 2nd method to use decorator