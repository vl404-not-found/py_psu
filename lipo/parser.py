from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Empty


class Parser:
    variables = {}

    def __init__(self):

        self.pg = ParserGenerator(
            [
                'NUMBER', 'SUM', 'SUB', 'SEMI_COLON',
                'PRINT', 'VAR',
                'ASSIGN', 'VALUE_SETTER',
                'OPEN_PAREN', 'CLOSE_PAREN',
            ]
        )

    def parse(self):
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        # @self.pg.production('expression : VAR')
        # def number(p):
        #     return Number(self.variables.get(p[0].value))

        @self.pg.production('values : VAR VALUE_SETTER expression')
        def update(p):
            self.variables.update({p[0].value: p[2].value})
            return Number(self.variables.get(p[0].value))

        @self.pg.production('expression : ASSIGN VAR SEMI_COLON')
        @self.pg.production('expression : ASSIGN values SEMI_COLON')
        def setter(p):
            try:
                if p[1].gettokentype() == 'VAR':
                    self.variables.update({p[1].value: 0})
                    return Number(self.variables.get(p[1].value))
            except AttributeError:
                return Number(self.variables.get(p[1].value))

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def pro(p):
            if p[1].gettokentype() == 'SUM':
                return Sum(p[0], p[2])
            if p[1].gettokentype() == 'SUB':
                return Sub(p[0], p[2])

        @self.pg.production('expression : PRINT OPEN_PAREN VAR CLOSE_PAREN SEMI_COLON')
        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def ex(p):
            try:
                if p[2].gettokentype() == 'VAR':
                    return Print(self.variables.get(p[2].value))
            except AttributeError:
                return Print(p[2])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
