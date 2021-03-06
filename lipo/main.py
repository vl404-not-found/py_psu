from lipo.lexer import Lexer
from lipo.pr_parser import PrParser

if __name__ == '__main__':

    file_name = 'test.cry'
    pg = PrParser()
    pg.parse()
    parser = pg.get_parser()
    lexer = Lexer().get_lexer()
    lex = ''

    with open(file_name) as file:
        lines = file.read().splitlines()
        for line in lines:
            tokens = lexer.lex(line)
            # code2csvLexList
            # with open('out/test.csv', 'w+') as f:
            #     for t in tokens:
            #         lex += f' {t.name} | {t.value} \n'
            #     f.writelines(lex)
            #     print(lex)
            print(parser.parse(tokens))
