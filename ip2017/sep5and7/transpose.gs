
xpose0.l.n = [[x!!i|x<- l]| i <-[0...n-1]]

xpose1.[] = []
xpose1.([]::_)=[]
xpose1.l = map.head.l  ::  xpose1.(map.tail.l)

xpose.[].(m,n) = take.n.(repeat.[])
xpose.(x::xs).(m,n) = zipWith.(::).x.t
                 where
		   t = xpose.xs.(m,n)

