xpose.l = [ [x!!i |x<- l] |i<-[0...length.(head.l) -1]]

xpose1.[] =[[],[],[]]
xpose1.(x::xs) = zipWith.(::).x.(xpose1.xs)

xpose2.[] =repeat.[]
xpose2.(x::xs) = zipWith.(::).x.(xpose2.xs)

xpose3.l = foldr.(zipWith.(::)).(repeat.[]).l

xpose4.[]	= []
xpose4.([]::_)	= []
xpose4.l	= map. head. l :: xpose4.(map.tail.l)