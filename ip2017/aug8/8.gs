x. f = f+1

sum1.0 = 0
sum1.(n+1) = (n+ 1) + s
           where
	      s = sum1.n

app1.[].l2= l2
app1.(x::l1).l2 = x::p
    where
   p=app1.l1.l2


suml.[]		= 0
suml.(x::l)	= x + s
		 where
	           s = suml.l

len.[]		=0
len.(x::l)	=1+ s
                 where
		  s = len.l

rev.[]		= []
rev.(x::l)	= r ++ [x]
                 where
		  r = rev.l
