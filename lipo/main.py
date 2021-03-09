from lipo.lexer import Lexer

from lipo.parser import Parser

file_name = 'test.cry'
# file_name = 'index.cry'

with open(file_name) as file:
    input_file = file.read()
    file.close()

lexer = Lexer().get_lexer()
token = lexer.lex(input_file)

# for t in token:
#     print(f'Тип {t.name}, значение {t.value}')

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(token).eval()
