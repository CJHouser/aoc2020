import qualified Data.Text.IO as DTIO
import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Text (Text)
import Data.Void

type Parser = Parsec Void Text

-- Separate field name and value
-- Format: [a-b]:[#|a-b|A-B|0-9]
fieldParser :: Parser (String, String)
fieldParser = (,) <$> someTill lowerChar (char ':') <*> some (char '#' <|> alphaNumChar)

-- Separates field/values within passport
-- Format: FV[NEWLINE|SPACE]
passportParser :: Parser [(String, String)]
passportParser = endBy fieldParser (optional spaceChar)

-- Separates passports within input
-- Format: passport[2*NEWLINE|EOF]
inputParser :: Parser [[(String, String)]]
inputParser = sepBy passportParser spaceChar

main = do
    --parseTest fieldParser "aaa:#aaa000"
    --parseTest passportParser "aaa:#aaa000 bbb:#bbb111\nccc:#ccc222"
    --parseTest inputParser "aaa:#aaa000 bbb:#bbb111\nccc:#ccc222\n\nddd:#ddd333"
    let fd = "../inputs/d04"
    contents <- DTIO.readFile fd
    case runParser inputParser fd contents of Left x -> print x
                                              Right x -> print x
