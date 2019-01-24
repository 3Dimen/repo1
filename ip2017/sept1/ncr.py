def c(n,r):
    if r == 0:
        return [[]]
    elif len(n) == 0:
        return []
    else:
        return [[n[0]] + l for l in c(n[1:],r-1)] + c(n[1:],r)

def ce(n,r):
    return ([[]] if r == 0 else
            [] if n == [] else
            [[n[0]] + l for l in ce(n[1:],r-1)] + ce(n[1:],r)
            )


## Redo from list of lists to set of set

st = frozenset
nullset = st([])
def singleton(x): return st([x])
def splitset(s):
    i = iter(s)
    e = next(i)
    new = st(i)
    return e,new

def cs(n,r):
    if r == 0 :
        return singleton(nullset)
    elif len(n) == 0 :
        return nullset
    else:
        x,xs = splitset(n)
        return st([(singleton(x) | l) for l in cs(xs,r-1)]) | cs(xs,r)

def ss0n(fs):
    """ Shows a simple-set (ie set-0, contains no subsets) nicely"""
    r = "{"
    for x in fs:
        r += repr(x) + ", "
    return r + "}"

def ss1n(fs0):
    """ Shows a set-of-sets (ie set-1, contents are sets) nicely"""
    r = "{"
    for x in fs0:
        r += ss0n(x) + ", "
    return r + "}"    
