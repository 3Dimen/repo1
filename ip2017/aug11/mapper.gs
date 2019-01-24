--add1.[]=[]
--add1.(x::xs)=x+1::add1.xs

add1 = list_mapper.(+1)

--mul2.[]=[]
--mul2.(x::xs)=x*2::mul2.xs
mul2 = list_mapper.(*2)

--lord.[]=[]
--lord.(x::xs)=ord.x::lord.xs
lord = list_mapper.ord

--list_mapper:(Int-> Int) -> ([Int]-> [Int])
list_mapper.f = each
  where
    each.[]=[]
    each.(x::xs)=f.x::each.xs

