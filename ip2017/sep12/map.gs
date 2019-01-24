map0.f.[]	= []
map0.f.(x::xs)	= f.x :: map0.f.xs

map1.f = a
  where
     a.[]		= []
     a.(x::xs)  	= f.x :: a.xs

map2.f = a
  where
     a.l = if l == [] then [] else f.(head.l) ::  a.(tail.l)
     
map3.f = a
  where
     a = \l -> if l == [] then [] else f.(head.l) ::  a.(tail.l)

map4.f =  \l -> if l == [] then [] else f.(head.l) :: (map4.f).(tail.l)
