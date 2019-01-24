
sum1.[] = 0
sum1.(x::xs) = x + sum1.xs


mul1.[] = 1
mul1.(x::xs) = x * mul1.xs


len1.[] = 0
len1.(x::xs) = 1 + len1.xs

myand.[] = True
myand.(x::xs) = x && myand.xs

--list_reduce: (Int->Int->Int) -> Int -> ([Int]->Int)
list_reduce.op.id = sum2
  where
     sum2.(x::xs) = op.x.undefined

list_reduce.op.id.(x::xs) = op.x.undefined




sum3.(x::xs) = op2.x.(sum3.xs)
op2.x.y = undefined
lenop.x.y = 1 + y

f.x = 4
g.x = x

--h.x = y

q.x = undefined