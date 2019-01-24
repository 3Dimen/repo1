import os, os.path

# startDir = "/"

# directories = [startDir]
# while len(directories)>0:
#     directory = directories.pop()
#     for name in os.listdir(directory):
#         fullpath = os.path.join(directory,name)
#         if os.path.isfile(fullpath):
#             print fullpath                # That's a file. Do something with it.
#         elif os.path.isdir(fullpath):
#             directories.append(fullpath)  # It's a directory, store it.

from os import listdir
from os.path import isdir, isfile, join
def mywalk(fpath):  #full-path
    fulllist = listdir(fpath)
    files = [x for x in fulllist if isfile(x)]
    dirs = [x for x in fulllist if isdir(x)]
    for x in files: yield x
    for x in dirs:
        mywalk(join(fpath,x))
    
