# Lecture about FileIO (File handling)
###########################################################
# Python provides ways to manipulate different files 
# Different methods and techiques to create, edit and modify files

# When we want to open and read from a new txt file 
file = open('test_file.txt', 'r')
text = file.read()
print(text)
file.close

# We can use 'with' statement it automatically closes the files.
with open('test_file.txt', 'r') as reading_test_file:
    reading_test_file = reading_test_file.read()
    print(reading_test_file)
    
# When we write in a file, the file will automatically be created if it doesnot exist
# While writing, the older contents can be overwitten if you choose a pre-existing file
new_file = open('new_test_file.txt', 'w')
new_file.write("Hello This is a new test_file!")
print(new_file)
new_file.close
with open('test_file.txt', 'w') as test_file:
    test_file = test_file.write("This is appended using 'with/as statement'")
