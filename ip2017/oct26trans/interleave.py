def process(s1, s2):
    for x,y in zip(s1,s2):
       print(x.strip())
       print(y.strip())
if __name__ == '__main__':
    from sys import argv
    if len(argv) != 3:
        print("Two file args required")
        exit(1)
    with open(argv[1]) as f:
        s1 = f.readlines()
    with open(argv[2]) as f:
        s2 = f.readlines()

        process(s1, s2)
