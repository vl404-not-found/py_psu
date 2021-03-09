from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.ignore(r'\s+')

        self.lexer.add('ASSIGN', r'Var')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('COMMA', r',')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('SUM', r'\+')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('VALUE_SETTER', r'=')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('VAR', r'[a-zA-Z]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
