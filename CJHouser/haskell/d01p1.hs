import System.IO

-- Create a list containing the complement for each respective tail element.
-- If the head is a complement, it will be in the created complement list.
-- ###TODO###
-- Perhaps use helper function so map only needs to run once?
solution :: (Eq i, Num i) => [i] -> i
solution [] = (-1)
solution (x:xs)
    | elem x cs = x * target x
    | otherwise = solution xs
    where
        cs = map target xs
        target = (2020 -)

-- Boilerplate
main = do
    contents <- readFile "../inputs/d01"
    let result = solution $ map (read :: String -> Int) $ lines contents
    print result
