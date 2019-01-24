def process(l):
    l0= l[0::2]
    l1= l[1::2]
    for x in l0:
       print(x.strip())
    for x in l1:
       print(x.strip())


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        print("No file")
        exit(1)
    with open(argv[1]) as f:
        l = f.readlines()
    process(l)    
