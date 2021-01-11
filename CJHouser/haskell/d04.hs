import qualified Data.Text.IO as DTIO
import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Text (Text)
import Data.Void
import Data.Char

-- Check if all required fields are present.
part1 :: [(String, String)] -> Bool
part1 xs = let f x = (&&) (elem x (map fst xs))
           in foldr f True ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

-- Check if required fields are valid.
part2 :: (String, String) -> Bool
part2 ("cid", val) = True
part2 ("byr", val) = length val == 4 && elem (read val :: Int) [1920..2002]
part2 ("iyr", val) = length val == 4 && elem (read val :: Int) [2010..2020]
part2 ("eyr", val) = length val == 4 && elem (read val :: Int) [2020..2030]
part2 ("hgt", val) = let value = read (takeWhile isDigit val) :: Int
                         unit  = dropWhile isDigit val
                     in (unit == "cm" && elem value [150..193])
                        || (unit == "in" && elem value [59..76])
part2 ("hcl", val) = and [head val == '#',
                          length val == 7,
                          let f x = (&&) (isHexDigit x && (isLower x || isDigit x))
                          in foldr f True (tail val)]
part2 ("ecl", val) = elem val ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
part2 ("pid", val) = length val == 9
                     && foldr (\x -> (&&) (isDigit x)) True val
otherwise          = False

type Parser = Parsec Void Text

-- Separate field name and value
fieldParser :: Parser (String, String)
fieldParser = (,) <$> someTill lowerChar (char ':') <*> some (char '#' <|> alphaNumChar)

-- Separates field/values within passport
passportParser :: Parser [(String, String)]
passportParser = endBy fieldParser (optional spaceChar)

-- Separates passports within input
inputParser :: Parser [[(String, String)]]
inputParser = sepBy passportParser spaceChar

main = do
    --parseTest fieldParser "aaa:#aaa000"
    --parseTest passportParser "aaa:#aaa000 bbb:#bbb111\nccc:#ccc222"
    --parseTest inputParser "aaa:#aaa000 bbb:#bbb111\nccc:#ccc222\n\nddd:#ddd333"
    let filename = "../inputs/d04"
    contents <- DTIO.readFile filename
    case runParser inputParser filename contents of
        Left e -> print e
        Right xss -> do let p1 = filter part1 xss
                        let p2 = filter (foldr (\x -> (&&) $ part2 x) True) p1
                        print $ length $ p1
                        print $ length $ p2
