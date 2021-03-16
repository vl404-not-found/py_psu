from rply import ParserGenerator
from ast import Number, Sum, Sub, ExecuteString, Print


class Parser:

    def __init__(self):

        self.pg = ParserGenerator(
            [
                'NUMBER', 'SUM', 'SUB', 'SEMI_COLON',
                'PRINT', 'VAR'
                'COMMA', 'MUL', 'ASSIGN', 'VALUE_SETTER',
                'OPEN_PAREN', 'CLOSE_PAREN',
            ]
        )

    def parse(self):
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        # TODO: Допиши эту дрянь! (посмотри как правильно хранить переменные)
        @self.pg.production('expression : ASSIGN VAR VALUE_SETTER expression')
        def setter(p):
            print(p)
            return

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def pro(p):
            if p[1].gettokentype() == 'SUM':
                return Sum(p[0], p[2])
            if p[1].gettokentype() == 'SUB':
                return Sub(p[0], p[2])

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def ex(p):
            return Print(p[2])

        #
        # @self.pg.production(r'ASSIGN \w NUMBER \w')
        # def ex_assignee(p):
        #     print(r'i\'m here')
        #
        # @self.pg.production('expression : expression SUM expression')
        # @self.pg.production('expression : expression SUB expression')
        # def expression(p):
        #     left = p[0]
        #     right = p[2]
        #     operator = p[1]
        #     if operator.gettokentype() == 'SUM':
        #         return Sum(left, right)
        #     elif operator.gettokentype() == 'SUB':
        #         return Sub(left, right)
        #
        # @self.pg.production('ASSIGN expression : expression')
        # def assign(p):
        #     self.variables.update(p)
        # # @self.pg.production('Var expression : NUMBER')
        # # def var_assign():

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
