#!/usr/bin/python3
from local_lib.path import Path

def make_dir():
    dir = Path("new_dir").mkdir_p()
    file = "new_file.txt"

    with open(dir / file, 'w') as f:
        f.write('This is the new file...')

    with open(dir / file, 'r') as f:
        print("File content:\n", f.read())

if __name__ == "__main__":
    make_dir()