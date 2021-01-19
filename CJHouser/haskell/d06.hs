import System.IO

-- Counts the number of unique answers per group
part1 :: String -> [Char] -> Int
part1 [] acc = length acc                           -- Input finished
part1 ('\n':'\n':xs) acc = part1 xs [] + length acc -- Group finished: empty acc
part1 ('\n':xs) acc = part1 xs acc                  -- Skip whitespace
part1 (x:xs) acc                                    -- Add unique characters to acc
    | elem x acc = part1 xs acc
    | otherwise  = part1 xs (x:acc)

main = do
    contents <- readFile "../inputs/d06"
    let p1 = part1 contents []
    print p1
