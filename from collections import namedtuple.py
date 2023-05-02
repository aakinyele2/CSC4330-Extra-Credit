from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

class IfStatement:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
    
    def __str__(self):
        if_str = f'if ({self.condition}) {{\n'
        if_str += '\n'.join(str(statement) for statement in self.if_block)
        if_str += '\n}'
        if self.else_block:
            if_str += ' else {\n'
            if_str += '\n'.join(str(statement) for statement in self.else_block)
            if_str += '\n}'
        return if_str

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def consume(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            raise SyntaxError(f'Expected {token_type}, got {self.current_token}')
    
    def parse(self):
        if_statement = self.parse_if_statement()
        self.consume('EOF')
        return if_statement
    
    def parse_if_statement(self):
        self.consume('if')
        self.consume('(')
        condition = self.parse_expression()
        self.consume(')')
        if_block = self.parse_block()
        else_block = None
        if self.current_token and self.current_token.type == 'else':
            self.advance()
            else_block = self.parse_block()
        return IfStatement(condition, if_block, else_block)
    
    def parse_block(self):
        statements = []
        self.consume('{')
        while self.current_token and self.current_token.type != '}':
            statement = self.parse_statement()
            statements.append(statement)
        self.consume('}')
        return statements
    
    def parse_statement(self):
        if self.current_token.type == 'if':
            return self.parse_if_statement()
        else:
            raise SyntaxError(f'Unexpected token {self.current_token}')
    
    def parse_expression(self):
        # Dummy expression parsing
        return '1'
