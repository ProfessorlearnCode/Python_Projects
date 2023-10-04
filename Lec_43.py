# Lecture about Virtual Environment
##########################################################
# Virtual Environment is a tool used to isolate specific python environment on a single machine.

'''
A friend uses a package using V.1, but you use V.2. So there's a difference in versions.
So how do you run the code of your friend?
You can create a Virtual Environment of that Version so that your code can be ran

'''

# To create Virtual Environment
# --> python -m venv (Virtual_environment name)

# To activate Virtual Environment
# --> (Virtual_environment name)\Scripts\activate.bat



'''
If you want to send the project packages to your friend with the code
rather than sending all the details of each package you can send/export them 
using a '.txt file

'''

# Shows all the packages installed in an environment
# --> pip freeze > requirements.txt

# Installs all those packages in computer
# --> pip install -r requirements.txt