# Lecture about Sets and Set methods
#########################################
# Set is a datatype used to store multiple data and in which there is no repeating data
# Set are unordered and are enclosed by {}
# Sets are immutable (unchangeable)

s = {2, 4, 6, 2}        # Set will exclude any repeating values
print(s)            

info = {"Carla", 19, False, 5.9, 19}
print(info)             # They donot possess any specific order so the index may change while displaying

SET = {}                # The syntax for dict and set is rather similar
SET2 = set()            # The empty set is made like this
print(type(SET2))

for value in info:
    print(value)
    

# Set methods are used to manipulate data in the sets and even whole set structures

SET1 = {1, 2, 5, 6}
SET2 = {3, 6, 7}

print(SET1.union(SET2))                     # We can use mathematical operations on sets like Unions and intersection etc
print(SET1, SET2)

cities_europe = {"Madrid", "London", "Amsterdam", "Ankara", "Delhi"}
cities_asia = {"Lahore", "Kaula Lampur", "Mumbai", "Delhi"}

cities_union = cities_europe.union(cities_asia)                                 # Combine both sets excluding repeating terms
cities_europe.update(cities_asia)                                               # Updates S1 from the values of S2 excluding repeating terms
cities_intersection = cities_europe.intersection(cities_asia)                   # Takes Common from the both sets excluding repeating terms
cities_europe.intersection_update(cities_asia)                                  # Updates S1 from the values common in both S1 and S2 excluding repeating terms


# Symmetric Difference are the values that arenot common in the sets

cities_europe.difference(cities_asia)                                             # Gives the values that arenot common 
cities_europe.difference_update(cities_asia)                                      # Updates S1 with the the values that arenot common from S2 
print(cities_europe)

print(cities_europe.isdisjoint(cities_asia))                                      # Return Bool whether two sets doesnot have any matching value
print(cities_europe.issuperset(cities_asia))                                      # Return Bool whether S1 is a superset of S2
print(cities_europe.issubset(cities_asia))                                        # Return Bool whether S1 is a subset of S2
cities_asia.add("Singapore")                                                      # Used to add new entries in the set
cities_asia.update(cities_europe)                                                 # Used to update values for S1 from S2
cities_europe.remove("Madrid")                                                    # Remove a value which must be a part of Set
cities_europe.discard("Madrid")                                                   # Remove a value if it is a part of Set
poppedvalue = cities_europe.pop()                                                 # Takes a value out of the set
print(poppedvalue)
cities_asia.clear()                                                               # Clears the set empty
del cities_europe                                                                 # Deletes the set 

