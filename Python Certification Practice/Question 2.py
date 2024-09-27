#You are writing a function that works with files.
#You need to ensure that the function returns None if the file does not exist. If the file does exist, the function must return the first line.
#You write the following code:

import os
def get_first_line(filename, mode):

 #In which order should you arrange the code segments to complete the function?
    with open(filename, 'r') as file:
        if os.path.isfile(filename):
            return file.readline()
        else:
            return None
