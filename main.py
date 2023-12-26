#!/usr/bin/env python3

import sys
from parser import Parser

args = sys.argv[1:]

if len(args) != 1:
    print('[!] Error: invalid number of arguments')
    print('Usage: ./main.py <python-file>')
    exit(1)

if not args[0].endswith('.py'):
    print('[!] Error: invalid arguments')
    print('Usage: ./main.py <python-file>')
    print('You should only pass python files')
    exit(1)

class Colors:
    def __init__(self):
        self.colors = {
            'green': self.green,
            'red': self.red,
            'purple': self.purple,
            'blue': self.blue,
            'yellow': self.yellow
        }

    def green(self, txt):
        return f'\033[0;32m{txt}\033[0m'

    def red(self, txt):
        return f'\033[0;31m{txt}\033[0m'

    def blue(self, txt):
        return f'\033[0;36m{txt}\033[0m'

    def purple(self, txt):
        return f'\033[0;35m{txt}\033[0m'

    def yellow(self, txt):
        return f'\033[0;33m{txt}\033[0m'

    def make(self, color, txt):
        return self.colors[color](txt)

def read_code(name):
    with open(name, 'r') as f:
        return f.readlines()

p = Parser(args[0])

colors = Colors()

for token in p.parse():
    text = token[0]

    if token[1] == 'function':
        text = colors.purple(token[0])
    elif token[1] == 'bracket':
        text = colors.yellow(token[0])
    elif token[1] == 'quote' or token[1] == 'string':
        text = colors.green(token[0])
    elif token[1] == 'keyword':
        text = colors.red(token[0])
    elif token[1] == 'number':
        text = colors.blue(token[0])
    elif token[1] == 'comma':
        text = colors.yellow(token[0])
    elif token[1] == 'comment':
        text = colors.green(token[0])

    print(text, end='')

