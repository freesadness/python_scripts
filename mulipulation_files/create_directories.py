import os
import sys
from pathlib import Path
from core.small_functions.foreach_functions import foreach, foreach_yield

print(f'current path: {sys.path[0]}')
# path = Path(r"test1/test/test/test")
# directory = r"\test\test\test\test"
# path = sys.path[0]+r"/test/test/test/test"
# print(path)
# os.makedirs(path)
# os.mkdir(path)


if __name__ == '__main__':
    parent_dir = input('enter the parent directory path: ')
    try:
        parent_dir = Path(fr'{parent_dir}') if parent_dir != '' else sys.path[0]
        print(f'set current path or prefix with {parent_dir}')
    except ValueError:
        parent_dir = sys.path[0]
        print('not a value path. set to current path')
    directories = input("enter directories(start with '/' ,separate with ','): ")
    directories = directories.replace(' ', '').split(',')
    foreach(print, directories)
    # current_dir = sys.path[0]
    concat_paths = (lambda x: str(parent_dir) + str(Path(fr'{x}')))
    directories = foreach_yield(concat_paths, directories)
    result = list(directories)
    print(result)
    foreach(os.makedirs, result)
    # test = str(Path(r'C:\Users\frees\Desktop\python_scripts\core\small_functions')) + str(Path(r"/Models"))
    # print((Path(r"/Models")))
    # print(test)
    # foreach(Path, directories)
