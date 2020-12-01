import System.IO

-- a + b + c = target
--     b + c = target - a
-- The second equation is identical to the problem in part 1.
solution _ [] = (-1)
solution target (x:xs)
    | sr > 0    = x * sr
    | otherwise = solution target xs
    where
        sr = part1 (target - x) xs

-- Create a list containing the complement for each respective tail element.
-- If the head is a complement, it will be in the created complement list.
-- ###TODO###
-- Perhaps use helper function so map only needs to run once?
part1 :: (Eq i, Num i) => i -> [i] -> i
part1 _ [] = (-1)
part1 target (x:xs)
    | elem x cs = x * tc x
    | otherwise = part1 target xs
    where
        cs = map tc xs
        tc = (target -)

-- Boilerplate
main = do
    contents <- readFile "../inputs/d01"
    let result = solution 2020 $ map (read :: String -> Int) $ lines contents
    print result
