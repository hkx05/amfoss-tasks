main :: IO ()
main = do
    n <- readLn
    mapM_ print [i | i <- [2..n-1], isPrime i]
    
isPrime :: Int -> Bool
isPrime i = all (\b -> i `mod` b /= 0) [2..i-1]
