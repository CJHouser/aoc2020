import System.IO
import Text.ParserCombinators.Parsec
import Text.Printf

part1 :: [String] -> Bool
part1 []= False
part1 (l:h:c:cs:[]) =
    let count   = length $ filter (ch==) cs
        lo      = read l :: Int
        hi      = read h :: Int
        ch      = head c
    in (lo <= count) && (count <= hi)

part2 :: [String] -> Bool
part2 [] = False
part2 (l:h:c:cs:[]) =
    let lo      = (read l :: Int) - 1
        hi      = (read h :: Int) - 1
        ch      = head c
        xor a b = a /= b
    in xor (ch == cs !! lo) (ch == cs !! hi)

aocFile = endBy line eol
line = sepBy cell (oneOf "- ")
cell = many (noneOf "- \n")
eol = char '\n'

parseAOC :: String -> Either ParseError [[String]]
parseAOC input = parse aocFile "(unknown)" input

main = do
    contents <- readFile "../inputs/d02"
    let entries = parseAOC contents
    let p1 = either (\err -> (-1)) (\msg -> length $ filter part1 msg) entries
    let p2 = either (\err -> (-1)) (\msg -> length $ filter part2 msg) entries
    printf "Part 1: %d\n\rPart 2: %d\n\r" p1 p2
