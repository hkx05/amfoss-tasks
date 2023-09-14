main :: IO ()
main = do
    n <- readLn
    mapM_ print [i | i <- [2..n-1], isPrime i]
    --The mapM_ function is used to apply the print function to each element in the list.--

isPrime :: Int -> Bool
isPrime i = all (\b -> i `mod` b /= 0) [2..i-1]
