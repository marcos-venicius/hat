class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.keywords = set(['import', 'as', 'from', 'class', 'for', 'elif', 'if', 'else', 'def', 'in', 'return', 'not', 'while', 'True', 'False', 'break'])

    def load_lines(self):
        with open(self.filename, 'r') as f:
            return f.readlines()

    def __parse_line(self, line):
        last_tokens = []

        token = ''
        lcl = []
        last_char = ''

        special_chars = set(["'", '.', '[', ']', '(', ')', '#', ' ', ',', '\n', '='])

        for char in line:
            if char in special_chars:
                if last_char == '#' and char != '\n':
                    last_char = '#'
                elif char == '.' and last_char == "'":
                    last_char = "'"
                else:
                    last_char = char

                lcl.append(last_char)

            if char not in special_chars:
                token += char
            elif last_char == '#':
                token += char
            elif char == '#':
                yield ('#', 'comment')
                token = ''
            elif char == '=':
                yield (token, 'text')
                yield (char, 'text')
                token = ''
            elif char == ' ':
                if token in self.keywords:
                    yield (token, 'keyword')
                else:
                    yield (token, 'text')

                yield (char, 'space')

                token = ''
            elif char == '.':
                if last_char != "'":
                    if token.isnumeric():
                        yield (token, 'number')
                        yield (char, 'number')
                    else:
                        yield (token, 'text')
                        yield (char, 'text')
                    token = ''
                else:
                    token += char
            elif char == '\n':
                if last_char == '#' or len(lcl) >= 2 and lcl[-2] == '#':
                    yield (token, 'comment')
                else:
                    yield (token, 'text')
                yield ('\n', 'breakline')
                token = ''
            elif char == '(':
                yield (token, 'function')
                yield (char, 'bracket')
                token = ''
            elif char == ')':
                if token.isnumeric():
                    yield (token, 'number')
                    yield (char, 'bracket')
                else:
                    yield (token, 'text')
                    yield (char, 'bracket')
                token = ''
            elif char == '[' or char == ']':
                if last_char == "'":
                    token += char
                else:
                    yield (token, 'text')
                    yield (char, 'bracket')
                    token = ''
            elif char == ',':
                if token.isnumeric():
                    yield (token, 'number')
                else:
                    yield (token, 'text')
                yield (char, 'comma')
                token = ''
            elif char == "'" and last_char != "'":
                yield (char, 'quote')
                token = ''
            elif char == "'" and last_char == "'":
                yield (token, 'string')
                yield (char, 'quote')
                token = ''

    def parse(self):
        lines = self.load_lines()

        for line in lines:
            yield from self.__parse_line(line)
