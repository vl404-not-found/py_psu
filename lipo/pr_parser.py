from rply import ParserGenerator


class PrParser:

    def __init__(self):
        self.pg = ParserGenerator(
            [
                'NUMBER', 'SUM', 'SUB', 'SEMI_COLON',
                'VAR', 'MUL', 'DIV',
                'ASSIGN', 'VALUE_SETTER',
                'OPEN_PAREN', 'CLOSE_PAREN', 'COMMA'
            ]
        )

    def parse(self):
        @self.pg.production('expression : ASSIGN exp_b SEMI_COLON')
        @self.pg.production('expression : ASSIGN exp_c SEMI_COLON')
        def exp():
            pass

        @self.pg.production('exp_b : exp_c COMMA exp_b')
        def exp_b():
            pass

        @self.pg.production('exp_c : VAR')
        def exp_c():
            pass

        @self.pg.production('expression : exp_c VALUE_SETTER exp_f SEMI_COLON')
        def exp_e():
            pass

        @self.pg.production('exp_f : SUB exp_g')
        @self.pg.production('exp_f : exp_g')
        def exp_f():
            pass

        # @self.pg.production('exp_g : exp_o')
        # @self.pg.production('exp_g : exp_g exp_k exp_g')
        # @self.pg.production('exp_g : OPEN_PAREN exp_f CLOSE_PAREN')
        # def exp_g():
        #     pass

        @self.pg.production('exp_o : exp_c')
        @self.pg.production('exp_o : NUMBER')
        def exp_o():
            pass

        @self.pg.production('exp_g : term SEMI_COLON')
        @self.pg.production('exp_g : exp_g SUM term SEMI_COLON')
        @self.pg.production('exp_g : exp_g SUB term SEMI_COLON')
        def p():
            pass

        @self.pg.production('term : factor SEMI_COLON')
        @self.pg.production('term : factor MUL factor SEMI_COLON')
        @self.pg.production('term : factor DIV factor SEMI_COLON')
        def p():
            pass

        @self.pg.production('factor : OPEN_PAREN exp_g CLOSE_PAREN SEMI_COLON')
        @self.pg.production('factor : exp_o SEMI_COLON')
        def p():
            pass

        # @self.pg.production('exp_k : SUM')
        # @self.pg.production('exp_k : SUB')
        # @self.pg.production('exp_k : MUL')
        # @self.pg.production('exp_k : DIV')
        # def exp_k():
        #     pass

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
