#You are creating a function that reads a data file and prints each line of the file.
#You write the following code. Line numbers are included for reference only.

import os
def read_file(file):
    line = None
    if os.path.isfile(file):
        data = open(file, 'r')
        while line != '':
            line = data.readline()
    print(line)