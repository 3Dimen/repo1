tk: [Int] -> Int -> [Int]
tk.(x::l).0=[]
--tk.[].n=undefined
tk.(x::l).n=x::s
  where s=tk.l.(n-1)

inner: [Int] -> [Int] -> Int
inner.[].[]=0
inner.l1.[]=undefined
inner.[].l1=undefined
inner.(x::l1).(y::l2)=(x*y)+inner.l1.l2

nth: [Int] -> Int -> Int
nth.[].n=undefined
--nth.l.0=undefined
nth.(x::l).0=x
nth.(x::l).n=nth.l.(n-1)