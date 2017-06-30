"""Archivo principal de calculadora."""
from analizador import parse

while True:
    try:
        exp_str = raw_input('analize> ')
    except EOFError:
        break
    print(parse(exp_str))
