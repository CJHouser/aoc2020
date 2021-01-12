import System.IO
import Data.List (foldl')
import Text.Printf

-- Convert the input to a useable, binary format.
toBin :: Char -> Int
toBin c
    | c == 'F'  = 0
    | c == 'L'  = 0
    | otherwise = 1

-- https://stackoverflow.com/a/26961027
toDec :: String -> Int
toDec = foldl' (\acc x -> acc * 2 + toBin x) 0

-- Calculate the seat ID for a boarding pass 
calcSID :: (String, String) -> Int
calcSID (rb, cb) = toDec rb * 8 + toDec cb

main = do
    contents <- readFile "../inputs/d05"
    let sids = map calcSID . map (splitAt 7) $ lines contents
    let maxsid = maximum sids -- Part 1
    let minsid = minimum sids
    let consecSum = div (maxsid * (maxsid + 1) - minsid * (minsid - 1)) 2
    let missing = consecSum - sum sids -- Part 2
    printf "Part1: %d\n\rPart2: %d\n\r" maxsid missing

