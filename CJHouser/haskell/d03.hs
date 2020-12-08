import System.IO
import Text.Printf

part1 :: Int -> Int -> [String] -> Int
part1 _ _ [] = 0
part1 col xdelta (x:xs)
    | c == '#' = 1 + rest
    | otherwise = 0 + rest
    where
        rest = part1 (col+xdelta) xdelta xs
        c = x !! (mod col (length x))

part2 :: [(Int, Int)] -> [String] -> Int
part2 _ [] = 0
part2 [] _ = 1
part2 ((xdelta, ydelta):slopes) xs
    | ydelta < 1 = 1
    | ydelta == 1 = (part1 0 xdelta xs) * rest
    | otherwise = (part1 0 xdelta (every ydelta xs)) * rest
    where
        rest = part2 slopes xs
        every elt =
            map snd . filter (\(lst,y) -> (mod lst elt) == 0) . zip [0..]

main = do
    contents <- readFile "../inputs/d03"
    let ls = lines contents
    let p1 = part1 0 3 ls
    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    let p2 = part2 slopes ls
    printf "Part 1: %d\n\rPart 2: %d\n\r" p1 p2

-- References:
-- https://stackoverflow.com/questions/39030173/every-n-th-element-of-a-list-in-the-form-of-a-list
