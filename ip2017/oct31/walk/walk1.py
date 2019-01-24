
import os, os.path


from os import listdir
from os.path import isdir, isfile, join

def walkpr(fpath):  #full-path
    # print("Fpath %s" % fpath)
    fulllist = listdir(fpath)
    files = [x for x in fulllist if isfile(join(fpath,x))]
    dirs = [x for x in fulllist if isdir(join(fpath,x))]
    # print("files %s dirs %s\n" % (files,dirs))
    for x in files: print("P: %s" % x)

    for d in dirs:
        x = join(fpath,d)
        print ("Entering rec with %s\n" % x)
        walkpr(x)


def mywalk(fpath):  #full-path
    #print("Call %s" % fpath)
    fulllist = listdir(fpath)
    files = [x for x in fulllist if isfile(join(fpath,x))]
    dirs = [x for x in fulllist if isdir(join(fpath,x))]

    #print("files %s \ndirs %s \nfulllist %s\n" % (files,dirs,fulllist))
    return files + [y  for x in dirs for y in mywalk(join(fpath,x))]

def walkit0(fpath):
    # print("Fpath %s" % fpath)
    fulllist = listdir(fpath)
    files = [x for x in fulllist if isfile(join(fpath,x))]
    dirs = [x for x in fulllist if isdir(join(fpath,x))]
    for f in files: yield f
    for x in dirs:
          for s in walkit0(join(fpath,x)):
              yield s

def walkit1(fpath):
    # print("Fpath %s" % fpath)
    fulllist = listdir(fpath)
    files = [x for x in fulllist if isfile(join(fpath,x))]
    dirs = [x for x in fulllist if isdir(join(fpath,x))]
    yield from files
    for x in dirs:
          (yield from walkit1(join(fpath,x)))

