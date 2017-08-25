import sys
import os
# you can add some start dir as param in sys.path.insert
sys.path.insert(0,'e:\\dev\\python')

# function run/execute given file
def run_file(file, dir = ''):
    '''
    if len(dir_in_python) > 0:    
        if dir_in_python[0] != '\\':
            dir_in_python = '\\' + dir_in_python
    '''
    my_path = os.path.join('e:\\dev\\python\\',dir, file)
    print(my_path)
    return exec(open(my_path).read())

