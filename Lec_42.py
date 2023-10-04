# Lecture about Enumerate Function
############################################################
# When working with index in for loop we can use Enumerate
# Enumerate gives you the value and the index at the same time 
# We can use it to unpack a tuple


marks = [12, 56, 32, 98, 1, 4, ]
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Lol")
    index += 1                  # We use index = 0 and the incretement it in the loop (1st method)

# We can use Enumerate for this function

for index, mark in enumerate(marks):
    print(f"{index}:{mark}")

for index, mark in enumerate(marks, start=1):
    print(f"{index}:{mark}")
    if index == 4:
        print(f"Highest num")