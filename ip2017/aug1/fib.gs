h.1 = 1
h.2 = 1
h.(n+2) = h.(n+1) + h.n

f.(a,b).1 = a
f.(a,b).2 = b
f.(a,b).n = f.(b,(a+b)).(n-1)

ff.n = f.(1,1).n

g.1 = (1,1)
g.(n+1) = (b,a+b)
   where (a,b) = g.n

gg.n = fst.(g.n)



fact. 0 = 1
fact.n = n * fact.(n-1)








fib = 1::1::zipWith.(+).fib.(tail.fib)
