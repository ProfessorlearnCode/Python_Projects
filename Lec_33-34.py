# Lecture about Dictionaries and Dictionary Methods
###################################################
# Dictionaries are ordered collection of data items
# It is a combination of Key : Value pairs
# They store various data in a variable


dictionary = {
    1 : "Ali",
    2 : "Haris",
    3 : "Farzam",
    4 : "Umar",
    5 : "Ahmad",
        
}

print(dictionary)                               # To print the whole dictionary
print(dictionary[2])                            # Return specific values using their keys and following a specific format else show error
print(dictionary.get(7))                        # Return specific values using their keys and following a specific format else show 'none'

for key in dictionary.keys():
    print(f"{key} : {dictionary[key]}")         # prints the keys from iterations

print(dictionary.items())
for key, value in dictionary.items():           # Using 'key','value' as iterables to store the values while iterations
    print(f"{key} ----> {value}")
    
# Dictionary Methods

senior = {
    "Shaveer" : 50,
    "Asim" : 70,
    "Asad" : 90,
    "Babar" : 91,
    "Saad" : 28,
}    

junior = {
    "Ali" : 22,
    "Usman" : 49,
    "Ahsan" : 87,
    "Umer" : 75,
    "Nouman" : 15,
}

senior.update(junior)                           # Updates Dic1 from the entries of Dic2
senior.clear()                                  # Clears the dic empty
senior.pop("Ali")                               # It seperates a specified entries from dic
del senior                                      # Deletes the dictionary




