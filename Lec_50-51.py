# Lecture about Reading, writing and some other methods while file handling
############################################################
# reading and writing methods allow us to either read or write within a file 
# read(), readline(),readlines() are some of them
# Similarly, we can use write(),writelines()

with open("test_file.txt", 'w') as file:
    file = file.write("Hello My name is Professor.\nI am 20 years old.\nThis is a test file")

f = open('test_file.txt', 'r')
i = 0

while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    
    stu1 = int(line.split(',')[0])
    stu3 = int(line.split(',')[2])
    stu2 = int(line.split(',')[1])
    print(f"marks of student{i}: {stu1}")
    print(f"marks of student{i}: {stu2}")
    print(f"marks of student{i}: {stu3}")


# We have written some lines in a text file
f = open('new_test_file.txt', 'w')
line = f.writelines("Line 1\nLine 2\nLine 3")
f.close()

# We are now reading the written contents
f_read = open('new_test_file.txt', 'r')
while True:
    reading = f_read.readline()
    if not reading:
        break
    print(reading.rstrip())
f.close()



# In seek() and tell() are used to work with file objects and their position within a file
# seek() moves the pointer to a certain position character
# tell() return the position within the current file, it tells us where are we after seek()

with open('new_test_file.txt', 'r') as read_file:
    print(type(read_file))
    read_file.seek(10)      # move to the 10th byte in the file
    print(read_file.tell())
    data = read_file.read(5)    # then, it reads the char from the 11th position
    print(data)

# truncate() is used to limit the number of content to a certain defined extent

with open('new_test_file.txt', 'w') as writing_file:
    writing_file.write("Hello, World!")
    writing_file.truncate(5)
    
with open('new_test_file.txt', 'r') as reading_file:
    reading = reading_file.readline()
    print(reading)
    
