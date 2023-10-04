# Lecture about __name__ == "__main__"
############################################################

import goodbye
'''
If you import a library and the library calls or uses the function which is in context 
to your current project then you can use the line to only run the function in the current program

--> if __name__ == '__main__':

__name__ == '__main__' is an idiom to determine whether the script is whether
being run direct or imported from another module



'''

if __name__ == '__main__':
    goodbye.main()

