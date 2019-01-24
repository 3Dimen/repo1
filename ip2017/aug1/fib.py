def h(n):
    if n == 1 or n == 2:
        return 1
    else:
        return h(n-1) + h(n-2)
