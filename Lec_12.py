# Lecture about String Theory, String Slicing and String methods (Part 1)
#####################################################################

names = "Farzam,Ali,Umair,Anus"
print("Length of the string is",len(names))         # Use len() to determine the number of characters in the string
print(names[0:6],"(With Zero index)")               # Index starts from 0 & ends on 6 (doesn't show 6th character)
print(names[:6],"(Without Zero index)")             # Python automatically starts the range from 0 index

fruit = "Mango"
len1 = len(fruit)                                   # Using len() to determine the number of letters in the Mango then storing it to len1 variable
print("Mango is a",len1,"letter word", end="\n")

Example = "MANGO"
spellinglen = len(Example)
print("Total number of letters in mango is",spellinglen)
print(Example[:])                                   # No range is specified so everything will be printed
print(Example[0:4])                                 # Range specified
print(Example[0:-3])                                # Y of Range will be subtracted from Total characters ==> New Range
print(Example[-1:-3],"Invalid Case")                # 1. X will be subtracted from Total characters then 2. Y will be subtracted from Total Characters, X<Y (Invalid)
print(Example[-3:-1])                               # 1. X will be subtracted from Total Characters then 2. Y will be subtracted from Total Characters, X>Y (Valid) 


# Quiz (Guess the output)
nm="Harry"
print([nm[-4:-2]])
