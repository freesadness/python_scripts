import os
import shutil
from math import ceil
from pathlib import Path
from core.small_functions.foreach_functions import foreach


def delete_directory(path, bytes_size_less_than=None):
    if Path(path).is_dir():
        if int(bytes_size_less_than) is None:
            shutil.rmtree(path)
        elif Path(path).stat().st_size > bytes_size_less_than:
            shutil.rmtree(path)


def remove_file(f):
    os.remove(f)
    print(f'deleted file: {f}')


def delete_files(path, bytes_size_less_than=None, suffix=None, or_choice=False):
    path = Path(path)
    files = get_files(path, bytes_size_less_than, suffix, or_choice)
    foreach(os.remove, files)
    for i in path.iterdir():
        if i.is_dir():
            files = get_files(i, bytes_size_less_than, suffix, or_choice)
            foreach(remove_file, files)
            delete_files(i)


def get_files(path, bytes_size_less_than=None, suffix=None, or_choice=False):
    paths = list()
    path = Path(rf'{path}')
    for i in path.iterdir():
        if i.is_file():
            paths.append(i)

    paths_met_size = set(
        filter(lambda p: True if bytes_size_less_than is None else Path(p).stat().st_size > bytes_size_less_than,
               paths))
    paths_met_suffix = set(filter(lambda p: True if suffix is None else p.suffix == suffix, paths))
    paths = paths_met_size & paths_met_suffix if or_choice or suffix else paths_met_size | paths_met_suffix

    map(str, paths)
    return paths


if __name__ == '__main__':
    print('if there is no input, it will try to delete everything')
    enter_path = input('enter a directory: ')
    enter_suffix = input('enter a suffix (enter skip delete all files): ')
    if enter_suffix == '':
        enter_suffix = None
    try:
        enter_size_less_than = int(input('enter size less than (enter skip delete all files): '))
    except ValueError:
        enter_size_less_than = None
    or_or_and: str = input('meet either or both? e/b')
    delete_files(rf'{enter_path}', bytes_size_less_than=enter_size_less_than, suffix=enter_suffix,
                 or_choice=True if or_or_and == 'e' else False)
