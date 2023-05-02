import re

# Define regular expressions for different token types
keywords = ['if', 'else', 'while', 'for', 'switch', 'case', 'break', 'continue', 'return', 'true', 'false']
operators = ['+', '-', '*', '/', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!']
symbols = ['{', '}', '(', ')', ';']
integer_literal = r'\d+'
real_literal = r'\d+\.\d+'
string_literal = r'"(?:\\.|[^"\\])*"'
boolean_literal = r'true|false'
identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'

patterns = {
    'keywords': '|'.join(keywords),
    'operators': '|'.join(re.escape(op) for op in operators),
    'symbols': '|'.join(re.escape(sym) for sym in symbols),
    'integer_literal': integer_literal,
    'real_literal': real_literal,
    'string_literal': string_literal,
    'boolean_literal': boolean_literal,
    'identifier': identifier,
}

pattern = re.compile('|'.join(f'(?P<{name}>{regex})' for name, regex in patterns.items()))

def tokenize(code):
    pos = 0
    while pos < len(code):
        match = pattern.match(code, pos)
        if match:
            token_type = match.lastgroup
            value = match.group(token_type)
            yield token_type, value
            pos = match.end()
        else:
            raise SyntaxError(f'Invalid token at position {pos}')
