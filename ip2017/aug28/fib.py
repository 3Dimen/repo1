def h(n):
    if n == 1 or n == 2:
        return 1
    else:
        return h(n-1) + h(n-2)

def h1(n):
    return (1   if (n == 1 or n == 2)   else   h1(n-1) + h1(n-2))

def g(n):
    if n==1:
        return (1,1)
    else:
        (a,b) = g(n-1)
        return (b,a+b)


    
    
def gg(n):
    return g(n)[0]

def gimp(n):
    a = 1
    b = 1
    for i in range(n-1):
#        a,b = b,a+b
        t = a
        a = b
        b = t + b
    return a




