#!/usr/bin/env python3
from regex import findall
from map import map
def oneline(l):
    llll = "".join(map[x] for x in findall(r'\X', l))
#    llll = [x for x in findall(r'\X', l)]
    print(llll)


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        print("No file")
        exit(1)
    with open(argv[1]) as f:
        s = f.read()
    oneline(s)
