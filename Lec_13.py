# Lecture about the String Theory and various string methods (Part 2)
#####################################################################

# Strings are immutable
a = "Farzam"
print(len(a))
print(a.capitalize())                             # Capitalize the 1st character and lowersize the rest of the string
print(a.upper())                                  # Uppercasing of the string
print(a.lower())                                  # Lowercasing of the string


strip = "AH !!"
print(strip.rstrip("!"))                          # Stripping certain Trailing Characters from the string 
strip2 = "!! AH"
print(strip2.rstrip("!"))                         # Stripping certain Leading Characters from the string


replace = "We know that Ali will be replaced with Akram"
print(replace.replace("Ali", "Akram"))            # Replacing all occurances of X with Y in the string


find = "He's an honest man. His name is Dan"
print(find.find("honest"))                          # Finds the 1st occurence of the specified parameter   


split = "Item1 Item2 Item3"
print(split.split(" "))                           # It splits the string with the parameter in the qoutations as marker     


center = "Using Center in Python"
print(len(center))
print(len(center.center(50)))                     # It aligns the string to the center as per given by the paramenter 


count = "This is a sentence, so this sentence is rather interesting"
print(count.count("sentence"))                    # It counts specified parameter in the string


ender = "Welcome to the console !!"
print(ender.endswith("!!"))                       # It provides a bool to see that the string ends with the specified parameter
ender2 = "Welcome to the console !!"
print(ender2.endswith("to", 4, 10))               # We can check a value in a string by providing a range 


Statement = "This is an alpha-num statement 12345678"
print(Statement.isalnum())                       # It returns 'Bool' if the entire string consists of only Alphanumeric (A-Z, a-z, 0-9) 
print(Statement.isalpha())                       # It returns 'Bool' if the entire string consists of only Alphabets (A-Z, a-z) 
print(Statement.isnumeric())                     # It returns 'Bool' if the entire string consists of only numeric (0-9)
print(Statement.isprintable())                   # It returns 'Bool' if the entire string is printable 
print(Statement.islower())                       # It returns 'Bool' if the entire string consists of only lowercase (a-z)
print(Statement.isupper())                       # It returns 'Bool' if the entire string consists of only uppercase (A-Z)      
print(Statement.istitle())                       # It returns 'Bool' if the 1st character of string is Capitalized
print(Statement.isspace())                       # It returns 'Bool' if the string consists of only spaces     
print(Statement.isdecimal())