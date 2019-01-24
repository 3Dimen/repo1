{-# LANGUAGE MonadComprehensions #-}
import Data.Set.Monad

set1 :: Set (Int,Int)
set1 = do 
         a <- fromList [1 .. 4]
         b <- fromList [1 .. 4]
         return (a,b)

-- Look a "set comprehension"
set2 :: Set (Int,Int)
set2 = [ (a,b) | (a,b) <- set1, even a, even b ]

emptyS :: Ord a => Set a
emptyS = fromList []
singletonS :: Ord a => a -> Set a
singletonS x = fromList [x]

c :: Ord a => Set a -> Integer -> Set (Set a)
c n 0 = singletonS emptyS
c [] r = emptyS
c (


-- c n 0 = 
