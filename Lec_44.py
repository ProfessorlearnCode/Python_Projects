# Lecture about importing 
#####################################################
# Importing in python is a process of loading code from python modules 
# We can use 'import' statement to import code 
# Once importing is successful you can easily use the functions and classes from that module


import math
 
number = input("Enter No: ")

math.sqrt(int(number))      # You can use module_name.Function_name to use it

# You can also import a specific part of the module using 'from' 
from math import pi

mult = int(number) * pi     # However I don't need to use the module name when using 'from'

