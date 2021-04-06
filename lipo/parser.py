from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Variable, Empty


class Parser:
    variables = {}

    def __init__(self):

        self.pg = ParserGenerator(
            [
                'NUMBER', 'SUM', 'SUB', 'SEMI_COLON',
                'PRINT', 'VAR', 'MUL', 'DIV',
                'ASSIGN', 'VALUE_SETTER',
                'OPEN_PAREN', 'CLOSE_PAREN',
            ]
        )

    def parse(self):
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : VAR')
        def variable(p):
            return Variable(self.variables.get(p[0].value))

        @self.pg.production('expression : VAR VALUE_SETTER expression SEMI_COLON')
        def update(p):
            self.variables.update({p[0].value: p[2].eval()})
            return Empty()

        @self.pg.production('expression : ASSIGN VAR VALUE_SETTER expression SEMI_COLON')
        def setter(p):
            self.variables.update({p[1].value: p[3].eval()})
            return Empty()

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def pro(p):
            if p[1].gettokentype() == 'SUM':
                return Sum(p[0], p[2])
            if p[1].gettokentype() == 'SUB':
                return Sub(p[0], p[2])
            if p[1].gettokentype() == 'MUL':
                return Sub(p[0], p[2])
            if p[1].gettokentype() == 'DIV':
                return Sub(p[0], p[2])

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def printing(p):
            return Print(p[2])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
