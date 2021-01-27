part1 :: (Eq a, Num a) => [a] -> [a] -> a
part1 xs (y:ys) = if findcomplement xs y
                     then part1 (tail (xs ++ [y])) ys
                  else y

findcomplement :: (Eq a, Num a) => [a] -> a -> Bool
findcomplement [] _ =  False
findcomplement (x:xs) y = (or $ map ((==) (y - x)) xs) || findcomplement xs y

main = do
    contents <- readFile "../inputs/d09"
    let nums = map read (lines contents)
    let len = 25
    print $ part1 (take len nums) (drop len nums)
