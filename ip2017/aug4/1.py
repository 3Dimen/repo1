
def f (l):

    newl = []
  
    while (l!=[]):
        (nm, roll, m1,m2) = l[0]
        newl =  [(nm, m1+m2)] + newl
        l = l[1:]
    return newl    
    
