pam : [a->b] -> a -> [b]
--map : (a->b) -> [a] -> [b]
--map.f.[]	= []
--map.f.(x::xs)	= f.x :: map.f.xs
--map.f.l       = [f.x | x <- l]
pam.[].x = []
pam.(f::fs).x=(f).x::pam.fs.x
pAm.fs.x = [f.x | f <- fs ]
--pAAm.fs.x  =  map.f.x |f<-fs

-- pam.[(1+),(2*), (6+)]. 3
-- [4,6,9]
prav.[].x  = []
prav.(f::fs).x = f.x :: prav.fs.x

pa3m.fs.x = map.(pec.x).fs
pa4m.fs.x = map.(.x).fs

pec.x.f = f.x