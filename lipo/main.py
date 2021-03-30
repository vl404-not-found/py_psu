from lipo.lexer import Lexer

from lipo.parser import Parser

if __name__ == '__main__':
    file_name = 'test.cry'
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    lexer = Lexer().get_lexer()

    with open(file_name) as file:
        # input_file = file.read()
        lines = file.read().splitlines()
        for line in lines:
            # print(line)
            tokens = lexer.lex(line)
            parser.parse(tokens).eval()
        file.close()

    # for t in token:
    #     print(f'Тип {t.name}, значение {t.value}')
