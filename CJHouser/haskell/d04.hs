import qualified Data.Text.IO as DTIO
import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Text (Text)
import Data.Void

-- Check if a passport has all the required fields. "cid" is ignored.
part1 :: [(String, String)] -> Bool
part1 xs = foldr f True ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    where keys      = map fst xs
          f key acc = (elem key keys) && acc

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
        Left x -> print x
        Right xs -> print $ length . filter id $ map part1 xs
